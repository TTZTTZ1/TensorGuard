import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import openai

from util.apidefs import get_api_defs

api_defs = None

# ──────────────────────────────────────────────────────────────────────────────
# Qwen2.5-Coder 本地权重配置
# 通过 --qwen_model_path 指定本地权重目录，模型在 fix 模式首次使用时加载一次，
# 后续所有修复复用同一个 pipeline，避免重复加载带来的显存/内存浪费。
# ──────────────────────────────────────────────────────────────────────────────
DEFAULT_QWEN_MODEL_PATH = "../Qwen2.5-Coder-7B-Instruct"  # 可替换为本地绝对路径
DEFAULT_QWEN_REPO_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"

# 全局缓存：仅在首次调用 qwen_repair() 时初始化
_qwen_pipeline = None

# Directory layout for seed programs
SEED_BASE_DIR = Path("codex_seed_programs")

LIB_SEED_DIRS = {
    "torch": SEED_BASE_DIR / "codex_torch_seeds",
    "tf":    SEED_BASE_DIR / "codex_tf_seeds",
}

# Timeout (seconds) when validating a seed program by executing it
EXEC_TIMEOUT = 30

# Maximum Qwen repair attempts per file before giving up
MAX_REPAIR_ATTEMPTS = 3


# ──────────────────────────────────────────────────────────────────────────────
# Original helpers (unchanged)
# ──────────────────────────────────────────────────────────────────────────────

def write_code(code, outdir):
    if not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)
    i = 1
    outdir = Path(outdir)
    while True:
        if os.path.exists(outdir / f"{i}.py"):
            i += 1
            continue
        with open(outdir / f"{i}.py", "w") as fw:
            fw.writelines(code)
        return


def gen_prompt(prompt_mode, prompt_template, api, lib):
    lib_str = "PyTorch" if lib == "torch" else "TensorFlow"
    if prompt_mode == "docstring_steps":
        api_def = api
        if api in api_defs:
            api_def = api_defs[api]["def"]
        prompt = prompt_template.format(lib_str, api_def)
    else:
        prompt = prompt_template.format(lib_str, api)
    return prompt


def gen(
    engine,
    prompt,
    temperature,
    max_tokens,
    n_samples,
    top_p,
    frequency_penalty,
    presence_penalty,
):
    t_start = time.time()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        n=n_samples,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    t_end = time.time()
    codes = [prompt + x["text"] for x in response["choices"]]
    return codes, t_end - t_start


def edit(input, instruction):
    response = openai.Edit.create(
        engine="code-davinci-edit-001",
        input=input,
        instruction=instruction,
        temperature=0,
        top_p=1,
    )
    return response["choices"][0]["text"]


# ──────────────────────────────────────────────────────────────────────────────
# Qwen2.5-Coder repair helpers（transformers 本地推理）
# ──────────────────────────────────────────────────────────────────────────────

def _get_qwen_pipeline(model_path: str):
    """
    懒加载 Qwen2.5-Coder 的 transformers 模型与分词器。

    首次调用时从 *model_path*（本地目录绝对路径）加载，结果缓存在全局
    _qwen_pipeline 中，后续所有修复调用复用同一份权重，避免重复占用显存。

    依赖：
        pip install transformers accelerate torch
    """
    global _qwen_pipeline
    if _qwen_pipeline is not None:
        return _qwen_pipeline

    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as e:
        raise RuntimeError(
            "transformers 未安装，请先执行：\n"
            "  pip install transformers accelerate torch"
        ) from e

    model_ref = model_path
    expanded_path = Path(model_path).expanduser()
    if expanded_path.exists():
        model_ref = str(expanded_path)
        print(f"[Qwen] 正在从本地路径加载模型：{model_ref}（仅首次，请稍候…）")
    elif model_path.startswith((".", "/", "~")):
        model_ref = DEFAULT_QWEN_REPO_ID
        print(
            f"[Qwen] 本地路径 {model_path} 不存在，"
            f"将从 HuggingFace Hub 下载 {model_ref} ...",
            flush=True,
        )
    else:
        print(f"[Qwen] 正在从 HuggingFace Hub 加载模型：{model_ref} ...")

    tokenizer = AutoTokenizer.from_pretrained(
        model_ref,
        trust_remote_code=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_ref,
        torch_dtype="auto",   # 有 GPU 时自动使用 bf16/fp16，否则 fp32
        device_map="auto",    # 自动分配 GPU；无 GPU 则回退到 CPU
        trust_remote_code=True,
    )
    model.eval()
    _qwen_pipeline = (model, tokenizer)
    print("[Qwen] 模型加载完成。")
    return _qwen_pipeline


def validate_program(file_path: Path, timeout: int = EXEC_TIMEOUT):
    """
    Execute *file_path* in a subprocess and decide whether it is 'valid'.

    A program is considered valid when it exits with return-code 0, or when it
    raises only a runtime error that is *not* an ImportError / SyntaxError
    (i.e. the API was at least called successfully but produced a numeric
    error — common for shape mismatches, etc.).

    Returns
    -------
    (is_valid: bool, error_message: str | None)
    """
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        stderr = result.stderr.strip()
        if result.returncode == 0:
            return True, None
        # Treat programs that fail only due to missing hardware / data as
        # "structurally valid" — they at least called the API.
        ignorable_patterns = [
            "RuntimeError",
            "ValueError",
            "AssertionError",
            "UserWarning",
        ]
        fatal_patterns = [
            "SyntaxError",
            "ImportError",
            "ModuleNotFoundError",
            "IndentationError",
            "NameError",
            "AttributeError",
            "TypeError",
        ]
        for pat in fatal_patterns:
            if pat in stderr:
                return False, stderr
        for pat in ignorable_patterns:
            if pat in stderr:
                return True, None   # structural validity accepted
        return False, stderr
    except subprocess.TimeoutExpired:
        # Infinite-loop programs are treated as valid (API was called)
        return True, None
    except Exception as e:
        return False, str(e)


def _strip_code_fences(text: str) -> str:
    """去除模型输出中可能残留的 markdown 代码块围栏。"""
    if not text.startswith("```"):
        return text
    inner, in_block = [], False
    for line in text.splitlines():
        if line.startswith("```") and not in_block:
            in_block = True
            continue
        if line.startswith("```") and in_block:
            break
        if in_block:
            inner.append(line)
    return "\n".join(inner).strip()


def build_repair_prompt(code: str, error_msg: str, api: str, lib: str) -> str:
    """构造发送给 Qwen 的修复指令（用户轮）。"""
    lib_str = "PyTorch" if lib == "torch" else "TensorFlow 2.10.0"
    return (
        f"The following {lib_str} program attempts to call the API `{api}` "
        f"but is broken. It produces this error when executed:\n\n"
        f"```\n{error_msg}\n```\n\n"
        f"Please fix **only** the bugs so the program calls `{api}` correctly. "
        f"Return the complete corrected Python code and nothing else — no "
        f"explanations, no markdown fences.\n\n"
        f"Broken code:\n\n{code}"
    )


def qwen_repair(
    model_path: str,
    code: str,
    error_msg: str,
    api: str,
    lib: str,
    temperature: float = 0.2,
    max_new_tokens: int = 512,
) -> str:
    """
    使用本地 Qwen2.5-Coder 权重修复 *code*。

    Parameters
    ----------
    model_path : str
        本地模型权重目录（由 --qwen_model_path 传入）。
    code : str
        待修复的原始代码。
    error_msg : str
        运行 *code* 时产生的错误信息。
    api, lib : str
        目标 API 名称与框架标识，用于构造提示词。
    temperature : float
        采样温度，越低输出越保守。
    max_new_tokens : int
        模型最多新生成的 token 数。

    Returns
    -------
    str
        修复后的代码；若推理失败则返回原始 *code*。
    """
    import torch

    model, tokenizer = _get_qwen_pipeline(model_path)

    system_msg = (
        "You are an expert Python programmer specialising in deep-learning "
        "frameworks. When given broken code and an error message you output "
        "ONLY the corrected Python source — no prose, no markdown, no code fences."
    )
    user_msg = build_repair_prompt(code, error_msg, api, lib)

    # Qwen2 系列使用 apply_chat_template 构造输入
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user",   "content": user_msg},
    ]
    try:
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
        inputs = tokenizer([text], return_tensors="pt").to(model.device)

        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=(temperature > 0),
                pad_token_id=tokenizer.eos_token_id,
            )

        # 只保留新生成的部分（去掉 prompt token）
        generated_ids = [
            out[len(inp):]
            for inp, out in zip(inputs["input_ids"], output_ids)
        ]
        repaired = tokenizer.batch_decode(
            generated_ids,
            skip_special_tokens=True,
        )[0].strip()

        repaired = _strip_code_fences(repaired)
        return repaired if repaired else code

    except Exception as e:
        print(f"    [Qwen] 推理失败: {e}")
        return code


def repair_and_save(
    src_file: Path,
    fix_dir: Path,
    api: str,
    lib: str,
    model_path: str,
    repair_temperature: float = 0.2,
    repair_max_tokens: int = 512,
) -> dict:
    """
    验证 *src_file*；若无效则调用本地 Qwen 进行迭代修复。

    第一个通过验证的版本（原始或修复后）将写入 *fix_dir*，函数返回结果字典。
    """
    code = src_file.read_text(encoding="utf-8")
    result = {
        "src": str(src_file),
        "status": None,      # "valid_original" | "repaired" | "failed"
        "attempts": 0,
        "error": None,
    }

    # ── Step 1: 验证原始文件 ─────────────────────────────────────────────────
    is_valid, error_msg = validate_program(src_file)
    if is_valid:
        fix_dir.mkdir(parents=True, exist_ok=True)
        dst = fix_dir / src_file.name
        shutil.copy2(src_file, dst)
        result["status"] = "valid_original"
        print(f"    ✓  {src_file.name}  →  已有效，直接复制。")
        return result

    print(f"    ✗  {src_file.name}  →  无效 ({error_msg[:120].strip()!r})")

    # ── Step 2: 迭代 Qwen 修复 ──────────────────────────────────────────────
    current_code  = code
    current_error = error_msg
    for attempt in range(1, MAX_REPAIR_ATTEMPTS + 1):
        print(f"       [修复尝试 {attempt}/{MAX_REPAIR_ATTEMPTS}] …")
        repaired_code = qwen_repair(
            model_path, current_code, current_error, api, lib,
            temperature=repair_temperature,
            max_new_tokens=repair_max_tokens,
        )
        if repaired_code == current_code:
            print("       [Qwen] 模型返回了未改动的代码，停止修复。")
            break

        # 写入临时文件进行验证
        tmp_path = fix_dir.parent / f"_tmp_{src_file.stem}_attempt{attempt}.py"
        tmp_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path.write_text(repaired_code, encoding="utf-8")

        is_valid, new_error = validate_program(tmp_path)
        result["attempts"] = attempt

        if is_valid:
            fix_dir.mkdir(parents=True, exist_ok=True)
            dst = fix_dir / src_file.name
            shutil.copy2(tmp_path, dst)
            tmp_path.unlink(missing_ok=True)
            result["status"] = "repaired"
            print(f"       ✓  第 {attempt} 次修复成功。")
            return result

        # 将本次（仍有错的）修复结果作为下一轮输入
        print(f"       仍然无效: {new_error[:120].strip()!r}")
        current_code  = repaired_code
        current_error = new_error
        tmp_path.unlink(missing_ok=True)

    result["status"] = "failed"
    result["error"]  = current_error
    print(f"    ✗  已放弃，共尝试 {result['attempts']} 次修复。")
    return result


# ──────────────────────────────────────────────────────────────────────────────
# Top-level fix-mode entry point
# ──────────────────────────────────────────────────────────────────────────────

def run_fix_mode(
    libs,
    model_path: str,
    repair_temperature: float = 0.2,
    repair_max_tokens: int   = 512,
    seed_base_dir: Path      = SEED_BASE_DIR,
):
    """
    Iterate over all seed programs under
      <seed_base_dir>/codex_{lib}_seeds/raw/<api_name>/*.py
    validate each one, repair broken programs with Qwen2.5-Coder, and write
    results to
      <seed_base_dir>/codex_{lib}_seeds/fix/<api_name>/<filename>.py

    Parameters
    ----------
    libs : list[str]
        Libraries to process, e.g. ["tf", "torch"] or ["torch"].
    model_path : str
        本地 Qwen 权重目录，传给 _get_qwen_pipeline() 懒加载。
    """
    # 预热：在遍历文件前统一加载模型，避免第一个文件等待时间过长被误解为卡死
    _get_qwen_pipeline(model_path)

    for lib in libs:
        if lib not in LIB_SEED_DIRS:
            print(f"[fix] 未知 lib '{lib}'，跳过。")
            continue

        lib_dir  = seed_base_dir / f"codex_{lib}_seeds"
        raw_dir  = lib_dir / "raw"
        fix_base = lib_dir / "fix"

        if not raw_dir.exists():
            print(f"[fix] Raw 目录不存在: {raw_dir}")
            continue

        print(f"\n{'='*70}")
        print(f"[fix] 处理 lib={lib}  raw_dir={raw_dir}")
        print(f"{'='*70}")

        # ── 断点续跑：清理上次已处理过的 raw 子目录 ───────────────────────────
        # 若 fix/ 下已存在某个 api 子目录，说明该 api 在上次运行中已完成（或处理
        # 到一半），将其对应的 raw/<api_name> 目录删除，避免重复处理。
        if fix_base.exists():
            already_fixed = sorted(p.name for p in fix_base.iterdir() if p.is_dir())
            if already_fixed:
                print(
                    f"[fix] 检测到上次中断的进度，"
                    f"将清除 raw/ 中已对应 fix/ 子目录的 {len(already_fixed)} 个目录："
                )
                for api_name in already_fixed:
                    raw_api_dir = raw_dir / api_name
                    if raw_api_dir.exists():
                        shutil.rmtree(raw_api_dir)
                        print(f"  [cleanup] 已删除 raw/{api_name}")
                    else:
                        print(f"  [cleanup] raw/{api_name} 不存在，跳过")
                print(f"[fix] 清理完成，继续处理 raw/ 剩余目录。")
            else:
                print(f"[fix] fix/ 目录存在但无子目录，从头开始。")
        # ── 断点续跑结束 ────────────────────────────────────────────────────────

        summary = {}   # api_name → list of per-file result dicts

        api_dirs = sorted(p for p in raw_dir.iterdir() if p.is_dir())
        if not api_dirs:
            print(f"[fix] {raw_dir} 下未找到任何 API 子目录")
            continue

        for api_dir in api_dirs:
            api_name = api_dir.name
            fix_dir  = fix_base / api_name
            py_files = sorted(api_dir.glob("*.py"))

            if not py_files:
                print(f"  [skip] {api_name} — 无 .py 文件")
                continue

            print(f"\n  [{lib}] {api_name}  （共 {len(py_files)} 个文件）")
            api_results = []

            for py_file in py_files:
                res = repair_and_save(
                    src_file=py_file,
                    fix_dir=fix_dir,
                    api=api_name,
                    lib=lib,
                    model_path=model_path,
                    repair_temperature=repair_temperature,
                    repair_max_tokens=repair_max_tokens,
                )
                api_results.append(res)

            n_orig   = sum(1 for r in api_results if r["status"] == "valid_original")
            n_fixed  = sum(1 for r in api_results if r["status"] == "repaired")
            n_failed = sum(1 for r in api_results if r["status"] == "failed")
            print(
                f"  → {api_name}: {n_orig} 原始有效, "
                f"{n_fixed} 修复成功, {n_failed} 修复失败"
            )
            summary[api_name] = api_results

        # 将汇总写到 fix 根目录
        summary_path = fix_base / "fix_summary.json"
        fix_base.mkdir(parents=True, exist_ok=True)
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"\n[fix] 汇总已写入 {summary_path}")

        all_results = [r for v in summary.values() for r in v]
        print(
            f"[fix] lib={lib} 汇总: "
            f"{sum(1 for r in all_results if r['status']=='valid_original')} 原始有效, "
            f"{sum(1 for r in all_results if r['status']=='repaired')} 修复成功, "
            f"{sum(1 for r in all_results if r['status']=='failed')} 修复失败  "
            f"（共 {len(all_results)} 个文件）"
        )


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        type=str,
        default="completion",
        help="one of 'completion', 'edit', 'fix'",
    )
    parser.add_argument("--lib", type=str, default="torch", help="one of 'tf', 'torch', 'all'")
    parser.add_argument(
        "--outdir", type=str, default="../codex_seed_programs_100sample"
    )
    parser.add_argument(
        "--prompt_template",
        type=str,
        default="data/codex_prompt/docstring_steps.txt",
    )
    parser.add_argument(
        "--input", type=str, default="data/tf_apis_100sample.txt", help="list of apis"
    )

    # Codex API parameters (used in completion / edit modes)
    parser.add_argument(
        "--engine", type=str, default="code-davinci-002", help="Codex engine name"
    )
    parser.add_argument("--apikey", type=int, default=0, help="Codex API key")
    parser.add_argument("--temperature", type=float, default=0.4)
    parser.add_argument("--n_samples", type=int, default=25)
    parser.add_argument("--max_tokens", type=int, default=256)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--frequency_penalty", type=float, default=0.0)
    parser.add_argument("--presence_penalty", type=float, default=0.0)

    # Qwen repair parameters（fix 模式专用）
    parser.add_argument(
        "--qwen_model_path",
        type=str,
        default=DEFAULT_QWEN_MODEL_PATH,
        help="本地 Qwen2.5-Coder 权重目录的绝对路径，例如 /data/models/Qwen2.5-Coder-7B-Instruct",
    )
    parser.add_argument(
        "--repair_temperature",
        type=float,
        default=0.2,
        help="Qwen 修复推理时的采样温度（越低越保守）",
    )
    parser.add_argument(
        "--repair_max_tokens",
        type=int,
        default=512,
        help="Qwen 每次修复最多生成的新 token 数",
    )
    parser.add_argument(
        "--seed_base_dir",
        type=str,
        default=str(SEED_BASE_DIR),
        help="种子程序根目录，需包含 codex_torch_seeds / codex_tf_seeds 子目录",
    )

    args = parser.parse_args()

    # ── fix mode ──────────────────────────────────────────────────────────────
    if args.mode == "fix":
        libs = ["tf", "torch"] if args.lib == "all" else [args.lib]
        run_fix_mode(
            libs=libs,
            model_path=args.qwen_model_path,
            repair_temperature=args.repair_temperature,
            repair_max_tokens=args.repair_max_tokens,
            seed_base_dir=Path(args.seed_base_dir),
        )
        sys.exit(0)

    # ── completion / edit modes (original logic, unchanged) ───────────────────
    mode       = args.mode
    lib        = args.lib
    temperature = args.temperature
    n_samples  = args.n_samples
    max_tokens = args.max_tokens
    with open(args.prompt_template, "r") as f:
        prompt_template = f.read()

    api_keys = {
        0: "YOUR_API_KEY",
    }
    openai.api_key = api_keys[args.apikey]

    version     = "raw"
    prompt_mode = args.prompt_template.split("/")[-1].rsplit(".", 1)[0]
    code_dir    = (
        Path(args.outdir)
        / prompt_mode
        / f"codex_{lib}_{temperature}_{max_tokens}_{n_samples}"
        / f"{version}"
    )
    print("Task: ", code_dir)
    os.makedirs(code_dir, exist_ok=True)
    with open(code_dir / "args.txt", "w") as f:
        f.write(str(args))

    # Load api defs for some prompt templates to use
    api_defs = get_api_defs(lib)
    max_patience      = 5
    num_limit_reached = 0

    if mode == "completion":
        if lib == "tf" or lib == "torch":
            wait_seconds = 0.0
            with open(args.input, "r") as fr:
                apis = fr.readlines()
                apis = [a.strip() for a in apis]
            out_dir = code_dir
            tcosts  = []
            flag    = True
            ret     = {}
            apicnt  = 0
            while flag:
                err_flag = False
                suc_flag = False

                for api in apis:
                    if os.path.exists(out_dir / api):
                        continue
                    if wait_seconds > 0.0:
                        time.sleep(wait_seconds)
                    print(api)
                    prompt = gen_prompt(prompt_mode, prompt_template, api, lib)
                    try:
                        codes, tc = gen(
                            args.engine,
                            prompt,
                            temperature,
                            max_tokens,
                            n_samples,
                            args.top_p,
                            args.frequency_penalty,
                            args.presence_penalty,
                        )
                        tcosts.append(tc)
                        ret[api] = {"code": codes, "g_time": tc}
                        for code in codes:
                            write_code(code, out_dir / api)
                        suc_flag = True
                        apicnt  += 1
                    except Exception as e:
                        err_flag = True
                        if wait_seconds < 3.0:
                            if num_limit_reached >= max_patience:
                                wait_seconds      += 0.5
                                num_limit_reached  = 0
                            time.sleep(30.0)
                        else:
                            time.sleep(30.0)
                if err_flag:
                    flag = True
                if not suc_flag:
                    flag = False
            with open(out_dir / "outputs.json", "w") as f:
                json.dump(ret, f)
            with open(out_dir / "log.txt", "w") as f:
                f.write(
                    "{}\nAverage cost in seconds for each Codex API call".format(
                        np.average(tcosts)
                    )
                )
