# 基线 C (完整方法)
#python qwen_seed.py --library torch --apilist data/torch_apis.txt --out_dir codex_seed_programs/torch-qwen --constraints_dir experiment/torch --ablation full

# 四个消融变体
#python qwen_seed.py --library torch --apilist data/torch_apis.txt --out_dir codex_seed_programs/torch-qwen/no_constraints --constraints_dir experiment/torch --ablation no_constraints
#python qwen_seed.py --library torch --apilist data/torch_apis.txt --out_dir codex_seed_programs/torch-qwen/no_repair      --constraints_dir experiment/torch --ablation no_repair
#python qwen_seed.py --library torch --apilist data/torch_apis.txt --out_dir codex_seed_programs/torch-qwen/no_layer4      --constraints_dir experiment/torch --ablation no_layer4
#python qwen_seed.py --library torch --apilist data/torch_apis.txt --out_dir codex_seed_programs/torch-qwen/no_resample    --constraints_dir experiment/torch --ablation no_resample
import argparse
import ast
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
import traceback
from typing import List, Optional, Tuple
import shutil

# 复用已有的清洗工具链
from process_file import (
    clean_code,
    syntax_fix_remove_last_line,
)
from util.util import ExecutionStatus

# =============================================================================
#                              消融实验配置
# =============================================================================
# 五种配置:
#   "full"           — 基线 C (本文完整方法): 结构化约束 + 四层修复 + 自适应重采样
#   "no_constraints" — w/o 结构化约束: 提示中移除 structured_info.txt 内容
#   "no_repair"      — w/o 四层修复管线: 仅保留 Layer 1 静态清洗
#   "no_layer4"      — w/o Layer 4: 保留 Layer 1-3, 关闭错误反馈重生成
#   "no_resample"    — w/o 自适应重采样: 强制 max_resample_rounds=1
ABLATION_CHOICES = ["full", "no_constraints", "no_repair",
                    "no_layer4", "no_resample"]


class AblationConfig:
    """单一开关集合, 在主流程中下传到 prompt 构造和修复函数."""
    def __init__(self, mode: str = "full"):
        assert mode in ABLATION_CHOICES, f"unknown ablation mode: {mode}"
        self.mode = mode
        self.include_constraints = (mode != "no_constraints")
        self.enable_layer2_to_4 = (mode != "no_repair")
        self.enable_layer4 = (mode not in ("no_repair", "no_layer4"))
        self.enable_resample = (mode != "no_resample")

    def __repr__(self):
        return (f"AblationConfig(mode={self.mode}, "
                f"constraints={self.include_constraints}, "
                f"L2-4={self.enable_layer2_to_4}, "
                f"L4={self.enable_layer4}, "
                f"resample={self.enable_resample})")

_MODEL = None
_TOKENIZER = None


# =============================================================================
#                       安全验证: 子进程 + 超时 + 强制 CPU
# =============================================================================

_VALIDATE_TIMEOUT_DEFAULT = 15  # 秒; 单条 seed 在 CPU 上的硬上限


def _safe_validate(
    code: str,
    library: str,
    timeout: int = _VALIDATE_TIMEOUT_DEFAULT,
) -> Tuple[ExecutionStatus, str]:
    """在隔离子进程里跑一段代码, 带超时 + 强制 CPU。"""
    prelude = ["import os",
            "os.environ['CUDA_VISIBLE_DEVICES'] = ''"]
    if library == "torch":
        prelude.append("import torch")
    elif library == "tf":
        prelude.append("os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'")
        prelude.append("import tensorflow as tf")
        prelude.append("tf.get_logger().setLevel('ERROR')")
    prelude.append("import numpy as np")
    full_code = "\n".join(prelude) + "\n" + code

    fd, tmp_path = tempfile.mkstemp(suffix=".py", prefix="qwseed_val_", dir="/tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(full_code)

        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = ""
        env["TF_CPP_MIN_LOG_LEVEL"] = "3"

        try:
            result = subprocess.run(
                [sys.executable, tmp_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                env=env,
                start_new_session=True,
            )
        except subprocess.TimeoutExpired:
            return ExecutionStatus.TIMEOUT, "validate-timeout"
        except Exception as e:
            return ExecutionStatus.EXCEPTION, f"subprocess-error: {e}"

        if result.returncode == 0:
            return ExecutionStatus.SUCCESS, ""

        stderr_msg = result.stderr.decode("utf-8", errors="replace")
        stdout_msg = result.stdout.decode("utf-8", errors="replace")
        err_msg = (stderr_msg or stdout_msg)[-2000:]

        if result.returncode in (132, 133, 134, 136, 137, 138, 139):
            return ExecutionStatus.CRASH, err_msg
        return ExecutionStatus.EXCEPTION, err_msg
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def _safe_recursive_clean(
    original: str,
    library: str,
    timeout: int = _VALIDATE_TIMEOUT_DEFAULT,
    max_trims: int = 30,
) -> str:
    """从尾部一行行裁剪直到能跑通。子进程隔离 + 上限, 不会卡死也不无限裁。"""
    code_lines = original.split("\n")
    for _ in range(min(len(code_lines), max_trims)):
        code = "\n".join(code_lines)
        if not code.strip():
            return ""
        status, _ = _safe_validate(code, library, timeout=timeout)
        if status == ExecutionStatus.SUCCESS:
            return code
        code_lines = code_lines[:-1]
    return ""


# =============================================================================
#                              Qwen 推理封装
# =============================================================================

def _load_qwen(model_path: str, dtype: str = "bfloat16") -> None:
    """本地加载 Qwen2.5-Coder-7B-Instruct。幂等，只加载一次。"""
    global _MODEL, _TOKENIZER
    if _MODEL is not None:
        return

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    t0 = time.time()
    print(f"[qwen_seed] loading {model_path} with dtype={dtype} ...", flush=True)

    torch_dtype = {
        "bfloat16": torch.bfloat16,
        "float16":  torch.float16,
        "float32":  torch.float32,
    }[dtype]

    _TOKENIZER = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    _MODEL = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch_dtype,
        device_map="auto",
        trust_remote_code=True,
    )
    _MODEL.eval()
    print(f"[qwen_seed] model loaded in {time.time() - t0:.1f}s", flush=True)


def _is_cuda_oom(exc: Exception) -> bool:
    """torch 不同版本里 OOM 类名不一致, 用消息匹配兜底。"""
    msg = str(exc).lower()
    return ("out of memory" in msg) or ("cuda oom" in msg)


def qwen_chat(
    system_prompt: str,
    user_prompt: str,
    n: int = 1,
    temperature: float = 0.4,
    top_p: float = 0.95,
    max_new_tokens: int = 512,
) -> List[str]:
    """以 chat-completion 风格调用 Qwen2.5-Coder，返回 n 条回复文本。"""
    import torch

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_prompt},
    ]
    text = _TOKENIZER.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = _TOKENIZER([text], return_tensors="pt").to(_MODEL.device)
    input_len = inputs["input_ids"].shape[1]

    outputs_text: List[str] = []
    remaining = n
    while remaining > 0:
        cur_n = remaining
        gen = None
        while cur_n > 0:
            try:
                with torch.no_grad():
                    gen = _MODEL.generate(
                        **inputs,
                        do_sample=True,
                        temperature=temperature,
                        top_p=top_p,
                        max_new_tokens=max_new_tokens,
                        num_return_sequences=cur_n,
                        pad_token_id=_TOKENIZER.eos_token_id,
                    )
                break
            except RuntimeError as e:
                if not _is_cuda_oom(e):
                    raise
                torch.cuda.empty_cache()
                if cur_n == 1:
                    print(f"[qwen_seed] CUDA OOM even at batch=1; "
                        f"giving up this generate() call.", flush=True)
                    return outputs_text
                cur_n = max(1, cur_n // 2)
                print(f"[qwen_seed] CUDA OOM, retrying with batch={cur_n}",
                    flush=True)
            except torch.cuda.OutOfMemoryError as e:
                torch.cuda.empty_cache()
                if cur_n == 1:
                    print(f"[qwen_seed] CUDA OOM even at batch=1; "
                        f"giving up this generate() call.", flush=True)
                    return outputs_text
                cur_n = max(1, cur_n // 2)
                print(f"[qwen_seed] CUDA OOM, retrying with batch={cur_n}",
                    flush=True)

        if gen is None:
            break

        for i in range(cur_n):
            new_tokens = gen[i][input_len:]
            outputs_text.append(
                _TOKENIZER.decode(new_tokens, skip_special_tokens=True)
            )
        remaining -= cur_n
        del gen
        torch.cuda.empty_cache()
    return outputs_text


# =============================================================================
#                        Prompt 构造 & 响应解析
# =============================================================================

SYSTEM_PROMPT = (
    "You are an expert Python programmer specialized in deep-learning libraries "
    "(PyTorch and TensorFlow). Given a target API, its signature, and its "
    "structured parameter constraints, produce a SHORT, SELF-CONTAINED Python "
    "snippet that (1) imports the library, (2) prepares valid input data "
    "satisfying every constraint, and (3) calls the target API exactly once. "
    "Respond with ONLY the Python code inside one ```python ... ``` block — "
    "no commentary, no explanation."
)


CONSTRAINT_FILENAME = "prompts/structured_info.txt"


def _constraint_block(constraint_path: str) -> str:
    """读取并原样返回 structured_info.txt 的 YAML-like 文本。"""
    if not os.path.isfile(constraint_path):
        return "# (no distilled constraints available for this API)"
    with open(constraint_path, "r") as f:
        return f.read().rstrip()


def build_seed_prompt(library: str, api: str, signature: str,
                    constraint_path: str,
                    include_constraints: bool = True) -> str:
    """组装 user-side prompt。include_constraints=False 用于消融。"""
    lib_name = "PyTorch" if library == "torch" else "TensorFlow"

    lines = [
        '"""',
        f"Task 1: import {lib_name}",
        f"Task 2: Generate input data",
        f"Task 3: Call the API {api}",
        signature,
    ]
    if include_constraints:
        lines.append(_constraint_block(constraint_path))
    lines.append('"""')
    lines.append("")
    return "\n".join(lines)


_CODE_BLOCK_RE = re.compile(r"```(?:python)?\s*\n(.*?)```", re.DOTALL)


def extract_code(raw_response: str) -> str:
    """从 Qwen 回复里提取第一段 ```python ... ``` 代码。"""
    m = _CODE_BLOCK_RE.search(raw_response)
    if m:
        return m.group(1).rstrip()
    return raw_response.strip()


# =============================================================================
#                             四层修复管线
# =============================================================================

def repair_seed(
    raw_code: str,
    api: str,
    library: str,
    qwen_fix_rounds: int = 1,
    enable_layer2_to_4: bool = True,
    enable_layer4: bool = True,
) -> Tuple[Optional[str], str]:
    """
    四层修复管线; 通过两个开关支持消融:
    enable_layer2_to_4=False -> 仅做 Layer 1 静态清洗, 之后直接判定
    enable_layer4=False      -> 保留 Layer 1-3, 关闭基于错误反馈的 Qwen 重生成
    status_tag: 'direct' | 'syntax-fix' | 'recursive' | 'qwen-fix' | 'dropped'
    """

    # --- Layer 1: 静态清洗 (始终执行) ---------------------------------------
    try:
        cleaned = clean_code(
            raw_code,
            prints_and_imports=False,
            comment=True,
            cuda=False,
            remove_func=False,
        )
    except Exception:
        cleaned = raw_code

    if not cleaned.strip():
        return None, "dropped"

    # --- 消融分支: w/o 四层修复管线 (仅 Layer 1) ----------------------------
    if not enable_layer2_to_4:
        status, _ = _safe_validate(cleaned, library)
        if status == ExecutionStatus.SUCCESS and _has_target_api(cleaned, api):
            return cleaned, "direct"
        return None, "dropped"

    # --- Layer 2 之前: 先判定 "direct" --------------------------------------
    # 正确语义: cleaned 自身能跑通就是 direct, 跟 unparse 是否改了格式无关.
    # 优化: 用便宜的 ast.parse 做语法预判, 仅当 cleaned 语法成立时才花一次
    # 子进程验证, 避免对必然失败的 case 浪费成本.
    cleaned_syntax_ok = True
    try:
        ast.parse(cleaned)
    except Exception:
        cleaned_syntax_ok = False

    if cleaned_syntax_ok:
        status, _ = _safe_validate(cleaned, library)
        if status == ExecutionStatus.SUCCESS and _has_target_api(cleaned, api):
            return cleaned, "direct"

    # --- Layer 2: 语法修复 ---------------------------------------------------
    syntax_fixed = syntax_fix_remove_last_line(cleaned)
    if not syntax_fixed.strip():
        return None, "dropped"

    status, _ = _safe_validate(syntax_fixed, library)
    if status == ExecutionStatus.SUCCESS and _has_target_api(syntax_fixed, api):
        return syntax_fixed, "syntax-fix"

    # --- Layer 3: recursive_clean (子进程版本) ------------------------------
    try:
        trimmed = _safe_recursive_clean(syntax_fixed, library)
    except Exception:
        trimmed = ""

    if trimmed and _has_target_api(trimmed, api):
        status, _ = _safe_validate(trimmed, library)
        if status == ExecutionStatus.SUCCESS:
            return trimmed, "recursive"

    # --- 消融分支: w/o Layer 4 ----------------------------------------------
    if not enable_layer4:
        return None, "dropped"

    # --- Layer 4: 报错反馈让 Qwen 重生成 ------------------------------------
    current = syntax_fixed
    for _ in range(qwen_fix_rounds):
        status, err_msg = _safe_validate(current, library)
        if status == ExecutionStatus.SUCCESS and _has_target_api(current, api):
            return current, "qwen-fix"
        if not err_msg:
            break

        fix_prompt = (
            f"The following Python snippet targeting `{api}` fails to execute.\n"
            f"Error message:\n{err_msg}\n\n"
            f"Broken code:\n```python\n{current}\n```\n\n"
            f"Please return a corrected, minimal, self-contained snippet that "
            f"still calls `{api}`. Respond with ONLY the corrected code inside "
            f"one ```python ... ``` block."
        )
        try:
            replies = qwen_chat(
                SYSTEM_PROMPT, fix_prompt,
                n=1, temperature=0.2, max_new_tokens=512,
            )
        except Exception as e:
            print(f"[qwen_seed] qwen_chat failed during fix: {e}", flush=True)
            break

        if not replies:
            break
        fixed_raw = extract_code(replies[0])
        try:
            current = clean_code(
                fixed_raw, prints_and_imports=False,
                comment=True, cuda=False, remove_func=False,
            )
            current = syntax_fix_remove_last_line(current)
        except Exception:
            continue

    status, _ = _safe_validate(current, library)
    if status == ExecutionStatus.SUCCESS and _has_target_api(current, api):
        return current, "qwen-fix"

    return None, "dropped"


def _has_target_api(code: str, api: str) -> bool:
    """粗略检查代码中是否调用了目标 API。"""
    last = api.split(".")[-1]
    return last in code


# =============================================================================
#                    API 签名与约束文件的轻量发现逻辑
# =============================================================================

def load_signature_file(path: str) -> dict:
    """加载 API 签名 txt 文件。"""
    db: dict = {}
    skipped: list = []
    sig_line_re = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_.]*)\s*\(")

    with open(path, "r") as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.rstrip()
            stripped = line.lstrip()
            if not stripped or stripped.startswith("#"):
                continue
            m = sig_line_re.match(line)
            if not m:
                skipped.append((lineno, line))
                continue
            api = m.group(1)
            sig = line.strip()
            if api in db:
                if db[api] != sig:
                    print(f"[qwen_seed] signature dup for {api!r} at "
                        f"line {lineno}; keeping first occurrence",
                        flush=True)
                continue
            db[api] = sig

    if skipped:
        print(f"[qwen_seed] {len(skipped)} unparseable line(s) in "
            f"{path}; first few:", flush=True)
        for lineno, line in skipped[:3]:
            print(f"  line {lineno}: {line!r}", flush=True)
    print(f"[qwen_seed] loaded {len(db)} signatures from {path}", flush=True)
    return db


def discover_signature(api: str, library: str,
                    signature_db: Optional[dict]) -> str:
    """签名来源优先级: 1) signature_file 2) inspect 3) `api(...)` 占位"""
    if signature_db and api in signature_db:
        return signature_db[api]

    try:
        parts = api.split(".")
        root = __import__(parts[0])
        obj = root
        for p in parts[1:]:
            obj = getattr(obj, p)
        import inspect
        sig = inspect.signature(obj)
        return f"{api}{sig}"
    except Exception:
        return f"{api}(...)"


def constraint_path_for(api: str, constraints_dir: str) -> str:
    """约束文件路径: constraints_dir/<api>/structured_info.txt"""
    return os.path.join(constraints_dir, api, CONSTRAINT_FILENAME)


# =============================================================================
#                             主流程
# =============================================================================

def _count_existing_valid(fix_dir: str) -> int:
    """断点续跑用: 数一下 fix_dir/*.py 已有几条。"""
    if not os.path.isdir(fix_dir):
        return 0
    return len([f for f in os.listdir(fix_dir) if f.endswith(".py")])


def generate_for_api(
    api: str,
    library: str,
    out_root: str,
    constraints_dir: str,
    signature_db: Optional[dict],
    n_samples_initial: int = 30,
    min_valid: int = 15,
    max_resample_rounds: int = 3,
    temperature: float = 0.4,
    qwen_fix_rounds: int = 1,
    ablation: AblationConfig = None,
    per_api_budget: Optional[float] = None,
    force_redo: bool = False,
) -> dict:
    """对单个 API 跑: 采样 -> 修复 -> 不足则补采样。"""
    raw_dir = os.path.join(out_root, "raw", api)
    fix_dir = os.path.join(out_root, "fix", api)

    existing = _count_existing_valid(fix_dir)
    if not force_redo and existing >= min_valid:
        print(f"[qwen_seed] [{api}] resume: already have "
            f"{existing} valid (>= {min_valid}); skip.", flush=True)
        return {
            "raw_tried": existing,
            "valid": existing,
            "unique_seeds": existing,
            "stats": {},
            "resumed": True,
        }

    for d in (raw_dir, fix_dir):
        if os.path.isdir(d):
            try:
                shutil.rmtree(d)
                print(f"[qwen_seed] [{api}] removed existing dir: {d}",
                    flush=True)
            except OSError as e:
                print(f"[qwen_seed] [{api}] WARNING: rmtree {d} failed: {e}",
                    flush=True)
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(fix_dir, exist_ok=True)

    if ablation is None:
        ablation = AblationConfig("full")

    effective_max_rounds = 1 if not ablation.enable_resample else max_resample_rounds

    signature = discover_signature(api, library, signature_db)
    cpath = constraint_path_for(api, constraints_dir)

    user_prompt = build_seed_prompt(
        library, api, signature, cpath,
        include_constraints=ablation.include_constraints,
    )

    valid_bank: List[str] = []
    seen_bodies = set()
    stats = {"direct": 0, "syntax-fix": 0, "recursive": 0,
            "qwen-fix": 0, "dropped": 0}
    raw_counter = 0
    api_t0 = time.time()

    for round_idx in range(effective_max_rounds):
        if per_api_budget is not None and (time.time() - api_t0) > per_api_budget:
            print(f"[qwen_seed] [{api}] per-API budget {per_api_budget}s "
                f"exhausted at round {round_idx}; stop.", flush=True)
            break

        cur_temp = temperature if round_idx == 0 else min(0.95, temperature + 0.3 * round_idx)
        need = n_samples_initial if round_idx == 0 else max(min_valid - len(valid_bank), 5) * 2

        print(f"[qwen_seed] [{api}] round {round_idx}: sampling {need} @ T={cur_temp:.2f}",
            flush=True)

        try:
            replies = qwen_chat(
                SYSTEM_PROMPT, user_prompt,
                n=need, temperature=cur_temp, max_new_tokens=512,
            )
        except Exception as e:
            print(f"[qwen_seed] [{api}] generation crashed: {e}", flush=True)
            traceback.print_exc()
            break

        for reply in replies:
            raw_counter += 1
            code = extract_code(reply)

            with open(os.path.join(raw_dir, f"{raw_counter}.py"), "w") as f:
                f.write(code)

            try:
                fixed, tag = repair_seed(
                    code, api, library, qwen_fix_rounds,
                    enable_layer2_to_4=ablation.enable_layer2_to_4,
                    enable_layer4=ablation.enable_layer4,
                )
            except Exception as e:
                print(f"[qwen_seed] [{api}] repair_seed unexpected error: {e}",
                    flush=True)
                traceback.print_exc()
                fixed, tag = None, "dropped"
            stats[tag] += 1
            if fixed is None:
                continue

            canonical = "\n".join(
                line.rstrip() for line in fixed.strip().splitlines() if line.strip()
            )
            if canonical in seen_bodies:
                continue
            seen_bodies.add(canonical)

            valid_bank.append(fixed)
            with open(os.path.join(fix_dir, f"{len(valid_bank)}.py"), "w") as f:
                f.write(fixed)

        print(f"[qwen_seed] [{api}] after round {round_idx}: "
            f"valid={len(valid_bank)} stats={stats}", flush=True)

        if len(valid_bank) >= min_valid:
            break

    return {
        "raw_tried": raw_counter,
        "valid": len(valid_bank),
        "unique_seeds": len(seen_bodies),
        "stats": stats,
        "resumed": False,
    }


# =============================================================================
#                      聚合指标: 首轮通过率 / 最终有效率 /
#                      平均唯一种子数 / API 覆盖率
# =============================================================================

def compute_aggregate_metrics(summary: dict, min_valid: int) -> dict:
    """
    从 summary (api -> per-api 统计 dict) 里聚合四个指标:

      1. 首轮通过率 (first-pass rate, 不经修复就跑通)
         = repair_seed 返回 'direct' 的比例.
         - micro: sum(stats['direct']) / sum(raw_tried)
         - macro: 各 API stats['direct']/raw_tried 的平均

      2. 最终有效率 (final validity rate)
         - micro: sum(valid) / sum(raw_tried)
         - macro: 各 API valid/raw_tried 的平均

      3. 平均唯一种子数 (avg unique seeds per API)
         - 所有参与 API 的 unique_seeds 的算术平均

      4. API 覆盖率 (API coverage rate)
         - strict: 满足 valid >= min_valid 的 API 占比
         - loose : 至少有 1 条 valid 的 API 占比

    备注:
    - "_aggregate" / "_*" 等以下划线开头的 key 视为元数据, 不参与聚合
    - 含 "error" 字段的条目 (该 API 跑挂了) 也跳过, 避免污染分母
    - 走断点续跑分支的 API (resumed=True) 没有本次 run 的 stats 拆分,
      因此不计入"首轮通过率"的分子分母, 但仍计入覆盖率/唯一种子数/最终有效率
    """
    api_entries = []
    for api, info in summary.items():
        if not isinstance(info, dict):
            continue
        if api.startswith("_"):
            continue
        if "error" in info:
            continue
        api_entries.append((api, info))

    n_apis = len(api_entries)
    if n_apis == 0:
        return {"n_apis": 0}

    # ---- 1) 首轮通过率 ------------------------------------------------------
    first_pass_pairs = [
        (info["raw_tried"], info["stats"].get("direct", 0))
        for _, info in api_entries
        if not info.get("resumed", False)
        and isinstance(info.get("stats"), dict)
        and info.get("raw_tried", 0) > 0
    ]
    sum_fp_tried = sum(t for t, _ in first_pass_pairs)
    sum_fp_direct = sum(d for _, d in first_pass_pairs)
    first_pass_micro = sum_fp_direct / sum_fp_tried if sum_fp_tried else 0.0
    first_pass_macro = (
        sum(d / t for t, d in first_pass_pairs) / len(first_pass_pairs)
        if first_pass_pairs else 0.0
    )

    # ---- 2) 最终有效率 ------------------------------------------------------
    final_pairs = [
        (info.get("raw_tried", 0), info.get("valid", 0))
        for _, info in api_entries
        if info.get("raw_tried", 0) > 0
    ]
    sum_tried = sum(t for t, _ in final_pairs)
    sum_valid = sum(v for _, v in final_pairs)
    final_rate_micro = sum_valid / sum_tried if sum_tried else 0.0
    final_rate_macro = (
        sum(v / t for t, v in final_pairs) / len(final_pairs)
        if final_pairs else 0.0
    )

    # ---- 3) 平均唯一种子数 --------------------------------------------------
    avg_unique = (
        sum(info.get("unique_seeds", info.get("valid", 0))
            for _, info in api_entries)
        / n_apis
    )

    # ---- 4) API 覆盖率 ------------------------------------------------------
    n_covered_strict = sum(
        1 for _, info in api_entries if info.get("valid", 0) >= min_valid
    )
    n_covered_loose = sum(
        1 for _, info in api_entries if info.get("valid", 0) >= 1
    )
    coverage_strict = n_covered_strict / n_apis
    coverage_loose = n_covered_loose / n_apis

    return {
        "n_apis": n_apis,
        "min_valid_threshold": min_valid,
        "sum_first_pass_tried":  sum_fp_tried,
        "sum_first_pass_direct": sum_fp_direct,
        "sum_raw_tried":         sum_tried,
        "sum_valid":             sum_valid,
        "first_pass_rate_micro": round(first_pass_micro, 4),
        "first_pass_rate_macro": round(first_pass_macro, 4),
        "final_validity_rate_micro": round(final_rate_micro, 4),
        "final_validity_rate_macro": round(final_rate_macro, 4),
        "avg_unique_seeds_per_api":  round(avg_unique, 2),
        "api_coverage_rate_strict":  round(coverage_strict, 4),
        "api_coverage_rate_loose":   round(coverage_loose, 4),
        "n_covered_strict":          n_covered_strict,
        "n_covered_loose":           n_covered_loose,
    }


def _print_aggregate_metrics(agg: dict) -> None:
    """把聚合结果按论文表格习惯打印到 stdout."""
    if agg.get("n_apis", 0) == 0:
        print("[qwen_seed] aggregate: no API entries to aggregate.", flush=True)
        return
    n = agg["n_apis"]
    print("\n[qwen_seed] ============ aggregate metrics ============",
        flush=True)
    print(f"  APIs aggregated:                {n}", flush=True)
    print(f"  min_valid threshold:            {agg['min_valid_threshold']}",
        flush=True)
    print(f"  首轮通过率 (micro, 不经修复):    "
        f"{agg['first_pass_rate_micro']:.2%}  "
        f"({agg['sum_first_pass_direct']}/{agg['sum_first_pass_tried']})",
        flush=True)
    print(f"  首轮通过率 (macro / per-API avg): "
        f"{agg['first_pass_rate_macro']:.2%}", flush=True)
    print(f"  最终有效率 (micro):              "
        f"{agg['final_validity_rate_micro']:.2%}  "
        f"({agg['sum_valid']}/{agg['sum_raw_tried']})", flush=True)
    print(f"  最终有效率 (macro / per-API avg): "
        f"{agg['final_validity_rate_macro']:.2%}", flush=True)
    print(f"  平均唯一种子数 / API:            "
        f"{agg['avg_unique_seeds_per_api']:.2f}", flush=True)
    print(f"  API 覆盖率 (valid >= min_valid): "
        f"{agg['api_coverage_rate_strict']:.2%}  "
        f"({agg['n_covered_strict']}/{n})", flush=True)
    print(f"  API 覆盖率 (valid >= 1):         "
        f"{agg['api_coverage_rate_loose']:.2%}  "
        f"({agg['n_covered_loose']}/{n})", flush=True)
    print("[qwen_seed] ===========================================\n",
        flush=True)


# 模块级 ref, 给 signal handler 用
_GLOBAL_SUMMARY: dict = {}
_GLOBAL_SUMMARY_PATH: Optional[str] = None


def _flush_summary_atomic(summary_dict: dict, path: str) -> None:
    """原子写: 先写 .tmp 再 os.replace, 中途被 kill 不留半截 JSON。"""
    tmp_path = path + ".tmp"
    with open(tmp_path, "w") as f:
        json.dump(summary_dict, f, indent=2)
    os.replace(tmp_path, path)


def _install_signal_handlers() -> None:
    """SIGTERM/SIGINT 触发时把当前 summary 落盘再退出。"""
    def _handler(signum, frame):
        print(f"\n[qwen_seed] caught signal {signum}; flushing summary "
            f"and exiting.", flush=True)
        if _GLOBAL_SUMMARY_PATH is not None:
            try:
                _flush_summary_atomic(_GLOBAL_SUMMARY, _GLOBAL_SUMMARY_PATH)
            except Exception as e:
                print(f"[qwen_seed] flush in signal handler failed: {e}",
                    flush=True)
        sys.exit(128 + signum)
    signal.signal(signal.SIGINT, _handler)
    signal.signal(signal.SIGTERM, _handler)


def main():
    # 把 _VALIDATE_TIMEOUT_DEFAULT 的 global 声明前置到 main 顶部:
    global _VALIDATE_TIMEOUT_DEFAULT

    parser = argparse.ArgumentParser(
        description="Qwen2.5-Coder-7B-Instruct seed generator "
                    "(replaces the Codex step)"
    )
    parser.add_argument("--model_path", type=str,
                        default="../Qwen2.5-Coder-7B-Instruct",
                        help="HuggingFace repo id OR local path.")
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["bfloat16", "float16", "float32"])
    parser.add_argument("--library", type=str, required=True,
                        choices=["torch", "tf"])
    parser.add_argument("--api", type=str, default=None,
                        help="Single API name; omit to use --apilist.")
    parser.add_argument("--apilist", type=str, default=None,
                        help="Path to a newline-separated list of API names.")
    parser.add_argument("--out_dir", type=str, required=True,
                        help="Output root, e.g. codex_seed_programs/pt-qwen . "
                            "Will create out_dir/raw/<api>/*.py and "
                            "out_dir/fix/<api>/*.py")
    parser.add_argument("--constraints_dir", type=str, required=True,
                        help="Root directory holding DeepSeek-distilled "
                            "constraints. Expected layout: "
                            "<constraints_dir>/<api>/structured_info.txt  "
                            "(e.g. constraints/torch.acosh/structured_info.txt)")
    parser.add_argument("--signature_file", type=str, default=None,
                        help="(optional) path to a plain-text signature file "
                            "scraped from official docs, one signature per "
                            "line like `tf.Assert(condition,data,...)`. "
                            "Typically one file per library, e.g. "
                            "torch_signatures.txt or tf_signatures.txt.")
    parser.add_argument("--n_samples", type=int, default=30,
                        help="Initial samples per API.")
    parser.add_argument("--min_valid", type=int, default=15,
                        help="Minimum number of valid fixed seeds per API.")
    parser.add_argument("--max_rounds", type=int, default=3,
                        help="Max resample rounds if min_valid is not met.")
    parser.add_argument("--temperature", type=float, default=0.4)
    parser.add_argument("--qwen_fix_rounds", type=int, default=1)
    parser.add_argument("--ablation", type=str, default="full",
                        choices=ABLATION_CHOICES,
                        help="Ablation mode. 'full' = 基线 C 完整方法; "
                            "'no_constraints' / 'no_repair' / 'no_layer4' / "
                            "'no_resample' 对应论文中的四个消融变体.")
    parser.add_argument("--per_api_budget", type=float, default=None,
                        help="单 API 墙钟时间上限(秒). 超时则停止补采样, 落盘已得结果. "
                            "默认 None 表示不限.")
    parser.add_argument("--force_redo", action="store_true", default=False,
                        help="忽略已有 fix/<api>/*.py, 强制重跑该 API.")
    parser.add_argument("--validate_timeout", type=int,
                        default=_VALIDATE_TIMEOUT_DEFAULT,
                        help="单条 seed 在子进程里的执行硬上限(秒). 默认 10s.")

    # 把 CLI 上的 validate_timeout 同步给模块级常量
    args = parser.parse_args()
    _VALIDATE_TIMEOUT_DEFAULT = args.validate_timeout

    if not args.api and not args.apilist:
        parser.error("Provide either --api or --apilist.")

    if args.apilist:
        with open(args.apilist, "r") as f:
            apis = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    else:
        apis = [args.api]

    sig_db = None
    if args.signature_file:
        if not os.path.isfile(args.signature_file):
            parser.error(f"--signature_file not found: {args.signature_file}")
        sig_db = load_signature_file(args.signature_file)
        missing = [a for a in apis if a not in sig_db]
        if missing:
            print(f"[qwen_seed] WARNING: {len(missing)}/{len(apis)} API(s) in "
                f"--apilist have no signature in {args.signature_file}; "
                f"will fall back to inspect/stub for them.",
                flush=True)
            for a in missing[:5]:
                print(f"  missing: {a}", flush=True)

    abl_cfg = AblationConfig(args.ablation)
    print(f"[qwen_seed] {abl_cfg}", flush=True)
    _load_qwen(args.model_path, args.dtype)

    os.makedirs(args.out_dir, exist_ok=True)
    summary_path = os.path.join(
        args.out_dir, f"qwen_seed_summary_{args.ablation}.json"
    )

    global _GLOBAL_SUMMARY, _GLOBAL_SUMMARY_PATH
    _GLOBAL_SUMMARY_PATH = summary_path
    _install_signal_handlers()

    if os.path.exists(summary_path):
        try:
            with open(summary_path, "r") as f:
                _GLOBAL_SUMMARY = json.load(f)
            print(f"[qwen_seed] resumed summary with "
                f"{len(_GLOBAL_SUMMARY)} entries from {summary_path}",
                flush=True)
        except Exception as e:
            print(f"[qwen_seed] failed to load existing summary "
                f"({e}); starting fresh.", flush=True)
            _GLOBAL_SUMMARY = {}

    summary = _GLOBAL_SUMMARY
    for i, api in enumerate(apis):
        print(f"\n=== [{i+1}/{len(apis)}] {api} ===", flush=True)
        try:
            result = generate_for_api(
                api=api,
                library=args.library,
                out_root=args.out_dir,
                constraints_dir=args.constraints_dir,
                signature_db=sig_db,
                n_samples_initial=args.n_samples,
                min_valid=args.min_valid,
                max_resample_rounds=args.max_rounds,
                temperature=args.temperature,
                qwen_fix_rounds=args.qwen_fix_rounds,
                ablation=abl_cfg,
                per_api_budget=args.per_api_budget,
                force_redo=args.force_redo,
            )
            summary[api] = result
            direct_n = result.get("stats", {}).get("direct", 0)
            print(f"[qwen_seed] [{api}] DONE: "
                f"valid={result['valid']}/{result['raw_tried']} "
                f"(direct={direct_n}, unique={result['unique_seeds']})",
                flush=True)
        except Exception as e:
            print(f"[qwen_seed] [{api}] FAILED: {e}", flush=True)
            traceback.print_exc()
            summary[api] = {"error": str(e)}

        try:
            _flush_summary_atomic(summary, summary_path)
        except Exception as e:
            print(f"[qwen_seed] WARNING: failed to flush summary after "
                f"{api}: {e}", flush=True)

        try:
            import torch
            torch.cuda.empty_cache()
        except Exception:
            pass

    agg = compute_aggregate_metrics(summary, args.min_valid)
    summary["_aggregate"] = agg
    try:
        _flush_summary_atomic(summary, summary_path)
    except Exception as e:
        print(f"[qwen_seed] WARNING: failed to flush final summary "
            f"with aggregate: {e}", flush=True)
    _print_aggregate_metrics(agg)

    print(f"\n[qwen_seed] summary written to {summary_path}", flush=True)


if __name__ == "__main__":
    main()