"""
prompt_input_ablation.py

为论文做一个 "文档输入 ablation" 对比实验:
对 data/fuzz4all.txt 中的 100 个 API (前 35 高约束, 36-70 中, 71-100 低),
分别用三种 prompt 模板让 Qwen2.5-Coder-7B-Instruct 各生成 30 个程序,
然后按 (filter 通过 + 子进程跑通) 的标准统计有效率与唯一程序数。

变体定义 (与 DL.py 中的提示词模板对应):
  A. 无文档输入  (no_input_prompt) — 只告诉模型 API 名字, 不喂任何文档
  B. 原始文档输入 (hw)             — 喂 greedy_prompt.txt (官方文档蒸馏的 NL 摘要)
  C. 结构化提示蒸馏 (auto_prompt)  — 在 B 之上叠加 structured_info.txt (参数约束)

最后输出 markdown 表:
| 变体 | 平均有效率 | 高约束 API | 中约束 API | 低约束 API | 唯一程序数 |

用法示例:
  python prompt_input_ablation.py \
      --apilist data/fuzz4all.txt \
      --constraints_dir experiment/torch \
      --out_dir ablation_runs/prompt_input \
      --model_path ../Qwen2.5-Coder-7B-Instruct
"""

import argparse
import ast
import csv
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
import traceback
from typing import Dict, List, Optional, Tuple

# =============================================================================
#                             基本常量与工具
# =============================================================================

# 与 DL.py 一致的系统消息
SYSTEM_MESSAGE = "You are a Deep Learning API Fuzzer"

# Fuzz4All 配置中的 separator / begin 默认值。这两个字段在原项目里来自 yaml
# 里的 target.trigger_to_generate_input / target.input_hint, 不同 config 文件
# 会有微调。这里给一组 DL 任务里最常见的合理默认, 用户可经 CLI 覆盖。
DEFAULT_SEPARATOR = "/* Please create a short Python program which uses the target API correctly. */"
DEFAULT_BEGIN = "import torch"

# 单个生成出来的子进程验证硬上限 (秒)。和 qwen_seed.py 默认一致。
DEFAULT_VALIDATE_TIMEOUT = 10

# 难度分组: 用户的约定 — 前 35 高, 36-70 中, 71-100 低 (1-indexed),
# 对应 0-indexed 是 [0,35), [35,70), [70,100)。
HIGH_END = 35
MID_END = 70


def load_apis(path: str) -> List[str]:
    """读取 fuzz4all.txt, 一行一个 API; 跳过空行 / 注释行。"""
    with open(path, "r", encoding="utf-8") as f:
        apis = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    return apis


def difficulty_of(idx: int) -> str:
    """0-indexed 在 apilist 中的位置 → 'high'/'mid'/'low'。"""
    if idx < HIGH_END:
        return "high"
    elif idx < MID_END:
        return "mid"
    else:
        return "low"


def read_text_or_none(path: str) -> Optional[str]:
    """文件不存在就返回 None, 让 caller 决定怎么 fallback。"""
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# =============================================================================
#                       Prompt 构造 — 三种变体, 对应 DL.py
# =============================================================================
#
# 设计要点:
#   * 三种 prompt 都用 chat-template 的 (system, user) 双消息形式喂给
#     Qwen2.5-Coder-Instruct, 因为它是 instruct 模型, 直接 completion 不如
#     chat 自然。
#   * user 消息内部仍然保留 Fuzz4All 风格的 docstring + separator + begin
#     结构, 这样模型行为和原 Fuzz4All 跑出来的同源数据可比。
#   * 末尾追加一行明确指令, 让模型把代码包在 ```python ... ``` 里, 便于解析。
#
# 三个变体之间唯一的差异就是 user 消息里 "信息载荷" 的多寡:
#   A 完全空    →  考验模型纯靠预训练知识能不能写对
#   B 喂自然语言摘要 → 类比 "看了人写的文档 README"
#   C 再加结构化约束 → 类比 "看了一份带类型/范围标注的 spec"

def _wrap_user(api: str, body: str, separator: str, begin: str) -> str:
    """共用尾部: separator + begin + 显式要求只输出一段 ```python``` 代码块。"""
    return (
        f"{body}\n"
        f"{separator}\n"
        f"{begin}\n\n"
        f"Please respond with ONLY one ```python ... ``` code block "
        f"that calls `{api}`, with all necessary imports."
    )


def build_prompt_A(api: str, separator: str, begin: str) -> Tuple[str, str]:
    """变体 A — no_input_prompt. 仅给 API 名字, 不提供任何文档。"""
    body = (
        f'"""\n'
        f"Generate a self-contained Python program that calls the API `{api}`.\n"
        f'"""'
    )
    return SYSTEM_MESSAGE, _wrap_user(api, body, separator, begin)


def build_prompt_B(api: str, greedy_text: str,
                   separator: str, begin: str) -> Tuple[str, str]:
    """变体 B — hw. 把 greedy_prompt.txt (NL 摘要) 当 docstring 喂进去。
    这对应 DL.py 的 wrap_prompt(prompt) 形式。"""
    body = f'"""\n{greedy_text.strip()}\n"""'
    return SYSTEM_MESSAGE, _wrap_user(api, body, separator, begin)


def build_prompt_C(api: str, structured_text: str, general_summary: str,
                   separator: str, begin: str) -> Tuple[str, str]:
    """变体 C — auto_prompt. 严格复刻 DL.py.wrap_dl_prompt 的字段顺序与分隔标记,
    确保和正式 fuzzing 跑时的 prompt 一字不差, 这样 ablation 结论可以直接
    解释当前论文里的方法 C 自身。"""
    body = (
        f"\n"
        f"# You are a Python code generation assistant for the `{api}` API.\n"
        f"\n"
        f"# First, here is a general summary of the API's functionality and usage:\n"
        f"---GENERAL SUMMARY START---\n"
        f"{general_summary.strip()}\n"
        f"---GENERAL SUMMARY END---\n"
        f"\n"
        f"# Second, here is a detailed, structured description of the API's "
        f"parameters and constraints. You MUST adhere to these rules.\n"
        f"---STRUCTURED INFO START---\n"
        f"{structured_text.strip()}\n"
        f"---STRUCTURED INFO END---\n"
    )
    return SYSTEM_MESSAGE, _wrap_user(api, body, separator, begin)


# =============================================================================
#                                Qwen 推理封装
# =============================================================================
# 风格与 qwen_seed.py 对齐: 懒加载 + chat template + OOM 自动减半重试。

_MODEL = None
_TOKENIZER = None


def _is_cuda_oom(exc: Exception) -> bool:
    msg = str(exc).lower()
    return ("out of memory" in msg) or ("cuda oom" in msg)


def load_qwen(model_path: str, dtype: str = "bfloat16") -> None:
    """幂等加载本地 Qwen 权重。"""
    global _MODEL, _TOKENIZER
    if _MODEL is not None:
        return

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    t0 = time.time()
    print(f"[ablation] loading {model_path} (dtype={dtype}) ...", flush=True)
    torch_dtype = {"bfloat16": torch.bfloat16,
                   "float16":  torch.float16,
                   "float32":  torch.float32}[dtype]

    _TOKENIZER = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    _MODEL = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch_dtype, device_map="auto",
        trust_remote_code=True,
    )
    _MODEL.eval()
    print(f"[ablation] model loaded in {time.time() - t0:.1f}s", flush=True)


def qwen_chat(
    system_prompt: str, user_prompt: str,
    n: int = 30, temperature: float = 0.4, top_p: float = 0.95,
    max_new_tokens: int = 512,
) -> List[str]:
    """以 chat 形式向 Qwen 索取 n 条采样。OOM 时自动二分 batch 重试,
    保证不会因为一次 30-batch 太大而整轮放弃。"""
    import torch
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user",   "content": user_prompt}]
    text = _TOKENIZER.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = _TOKENIZER([text], return_tensors="pt").to(_MODEL.device)
    input_len = inputs["input_ids"].shape[1]

    out: List[str] = []
    remaining = n
    while remaining > 0:
        cur = remaining
        gen = None
        while cur > 0:
            try:
                with torch.no_grad():
                    gen = _MODEL.generate(
                        **inputs, do_sample=True,
                        temperature=temperature, top_p=top_p,
                        max_new_tokens=max_new_tokens,
                        num_return_sequences=cur,
                        pad_token_id=_TOKENIZER.eos_token_id,
                    )
                break
            except (RuntimeError, torch.cuda.OutOfMemoryError) as e:
                # RuntimeError 里非 OOM 的种类要原样抛出, 否则会吞掉真问题
                if isinstance(e, RuntimeError) and not _is_cuda_oom(e):
                    raise
                torch.cuda.empty_cache()
                if cur == 1:
                    print("[ablation] OOM even at batch=1; abort this call.",
                          flush=True)
                    return out
                cur = max(1, cur // 2)
                print(f"[ablation] OOM, retry with batch={cur}", flush=True)

        if gen is None:
            break
        for i in range(cur):
            new_tokens = gen[i][input_len:]
            out.append(_TOKENIZER.decode(new_tokens, skip_special_tokens=True))
        remaining -= cur
        del gen
        torch.cuda.empty_cache()
    return out


_CODE_BLOCK_RE = re.compile(r"```(?:python)?\s*\n(.*?)```", re.DOTALL)


def extract_code(reply: str) -> str:
    """从模型回复里抓第一段 ```python ... ```; 没围栏就退化为整段去前后空白。"""
    m = _CODE_BLOCK_RE.search(reply)
    return m.group(1).rstrip() if m else reply.strip()


# =============================================================================
#                            过滤 / 验证 / 去重
# =============================================================================

def filter_has_api(code: str, api: str) -> bool:
    """与 DL.py.filter 等价: 全名命中, 或末段名后跟 ( 命中。"""
    if api in code:
        return True
    short = api.split(".")[-1]
    return bool(re.search(rf"\b{re.escape(short)}\s*\(", code))


def safe_validate(code: str, library: str = "torch",
                  timeout: int = DEFAULT_VALIDATE_TIMEOUT) -> str:
    """子进程隔离 + 超时 + 强制 CPU 验证, 返回字符串状态:
       'success'/'exception'/'crash'/'timeout'。
       这里强制 CPU 是因为我们关心的是 "代码语义是否合法", 不需要 GPU,
       同时避免 100+API × 3 variant × 30 sample 的并发挤爆显存。"""
    prelude = ["import os",
               "os.environ['CUDA_VISIBLE_DEVICES'] = ''"]
    if library == "torch":
        prelude.append("import torch")
    elif library == "tf":
        prelude.append("os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'")
        prelude.append("import tensorflow as tf")
        prelude.append("tf.get_logger().setLevel('ERROR')")
    prelude.append("import numpy as np")
    full = "\n".join(prelude) + "\n" + code

    fd, tmp = tempfile.mkstemp(suffix=".py", prefix="abl_val_", dir="/tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(full)
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = ""
        env["TF_CPP_MIN_LOG_LEVEL"] = "3"
        try:
            r = subprocess.run(
                [sys.executable, tmp],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                timeout=timeout, env=env, start_new_session=True,
            )
        except subprocess.TimeoutExpired:
            return "timeout"
        except Exception:
            return "exception"
        if r.returncode == 0:
            return "success"
        # 134=SIGABRT, 139=SIGSEGV 等, 是真崩 (有可能是 bug)
        if r.returncode in (132, 133, 134, 136, 137, 138, 139):
            return "crash"
        return "exception"
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def canonicalize(code: str) -> str:
    """归一化用于唯一程序数统计:
       1) 用 ast 解析后再 unparse 一次, 把空白 / 引号 / 冗余括号都打平
       2) 解析失败就退化为 strip 每行 + 去空行, 至少能挡住纯空白差异
       这样同一份程序仅因换行风格差异不会被多算成两份。"""
    try:
        node = ast.parse(code)
        return ast.unparse(node).strip()
    except Exception:
        lines = [ln.rstrip() for ln in code.splitlines() if ln.strip()]
        return "\n".join(lines)


# =============================================================================
#                           单 (api, variant) 跑批
# =============================================================================

def bench_one(
    api: str, variant: str,
    prompt_user: str, library: str,
    n_samples: int, temperature: float, top_p: float,
    validate_timeout: int,
    save_dir: str,
) -> Dict:
    """对单个 API 在某一变体下跑一轮采样 + 验证。
    返回 stats dict, 同时把 stats.json + 每个 raw/valid 程序落盘。"""
    raw_dir = os.path.join(save_dir, "raw")
    valid_dir = os.path.join(save_dir, "valid")
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    # 采样
    t0 = time.time()
    try:
        replies = qwen_chat(
            SYSTEM_MESSAGE, prompt_user,
            n=n_samples, temperature=temperature, top_p=top_p,
            max_new_tokens=512,
        )
    except Exception as e:
        print(f"[ablation] [{variant}/{api}] generation crashed: {e}",
              flush=True)
        traceback.print_exc()
        replies = []
    gen_time = time.time() - t0

    n_filtered = 0
    n_valid = 0
    valid_canon = set()
    status_breakdown = {"success": 0, "exception": 0,
                        "crash": 0, "timeout": 0}

    for i, reply in enumerate(replies):
        code = extract_code(reply)
        # 落盘 raw
        with open(os.path.join(raw_dir, f"{i}.py"), "w", encoding="utf-8") as f:
            f.write(code)

        # filter: 必须真的调用了目标 API, 否则就是 LLM 跑题
        if not filter_has_api(code, api):
            continue
        n_filtered += 1

        # 子进程验证
        status = safe_validate(code, library=library, timeout=validate_timeout)
        status_breakdown[status] += 1

        # 只有 success 才算入 valid
        if status == "success":
            n_valid += 1
            valid_canon.add(canonicalize(code))
            with open(os.path.join(valid_dir, f"{n_valid}.py"),
                      "w", encoding="utf-8") as f:
                f.write(code)

    n_unique = len(valid_canon)
    raw_n = len(replies)
    stats = {
        "api": api,
        "variant": variant,
        "n_samples_requested": n_samples,
        "n_samples_received":  raw_n,
        "n_filtered":          n_filtered,   # 通过 filter 的样本数
        "n_valid":             n_valid,      # filter+success 都通过
        "n_unique_valid":      n_unique,     # 唯一 valid 程序数
        "validity_rate":       (n_valid / raw_n) if raw_n > 0 else 0.0,
        "filter_rate":         (n_filtered / raw_n) if raw_n > 0 else 0.0,
        "status_breakdown":    status_breakdown,
        "gen_time_sec":        round(gen_time, 2),
    }
    with open(os.path.join(save_dir, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    return stats


# =============================================================================
#                           汇总: 按难度分组求平均
# =============================================================================

def aggregate(per_api_stats: List[Dict]) -> Dict:
    """per_api_stats: 单一 variant 下所有 api 的 stats 列表。
    返回 {avg, high_avg, mid_avg, low_avg, unique_total} (validity rates 已是百分比)。"""
    by_diff = {"high": [], "mid": [], "low": []}
    all_rates = []
    unique_total = 0
    for s in per_api_stats:
        diff = s["difficulty"]
        by_diff[diff].append(s["validity_rate"])
        all_rates.append(s["validity_rate"])
        unique_total += s["n_unique_valid"]

    def _mean_pct(xs):
        return (sum(xs) / len(xs) * 100.0) if xs else 0.0

    return {
        "avg":          _mean_pct(all_rates),
        "high_avg":     _mean_pct(by_diff["high"]),
        "mid_avg":      _mean_pct(by_diff["mid"]),
        "low_avg":      _mean_pct(by_diff["low"]),
        "unique_total": unique_total,
        "n_apis":       len(per_api_stats),
        "n_high":       len(by_diff["high"]),
        "n_mid":        len(by_diff["mid"]),
        "n_low":        len(by_diff["low"]),
    }


VARIANT_LABELS = {
    "A": "A. 无文档输入",
    "B": "B. 原始文档输入",
    "C": "C. 结构化提示蒸馏",
}


def write_summary(summary: Dict[str, Dict], out_dir: str) -> None:
    """落盘三份汇总文件: summary.json (机器可读) / summary.csv / summary.md。"""
    # 1. JSON: 全量
    with open(os.path.join(out_dir, "summary.json"), "w",
              encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # 2. CSV: 一行一变体, 适合丢到 Excel/Pandas
    csv_path = os.path.join(out_dir, "summary.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["变体", "平均有效率", "高约束 API",
                    "中约束 API", "低约束 API", "唯一程序数"])
        for vk in ["A", "B", "C"]:
            if vk not in summary:
                continue
            agg = summary[vk]["aggregate"]
            w.writerow([
                VARIANT_LABELS[vk],
                f"{agg['avg']:.1f}%",
                f"{agg['high_avg']:.1f}%",
                f"{agg['mid_avg']:.1f}%",
                f"{agg['low_avg']:.1f}%",
                agg["unique_total"],
            ])

    # 3. Markdown 表格 (用户要求的输出形式)
    md_path = os.path.join(out_dir, "summary.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Prompt 输入消融实验结果\n\n")
        f.write("| 变体 | 平均有效率 | 高约束 API | 中约束 API | "
                "低约束 API | 唯一程序数 |\n")
        f.write("|------|------------|------------|------------|"
                "------------|------------|\n")
        for vk in ["A", "B", "C"]:
            if vk not in summary:
                continue
            agg = summary[vk]["aggregate"]
            f.write(
                f"| {VARIANT_LABELS[vk]} | "
                f"{agg['avg']:.1f}% | "
                f"{agg['high_avg']:.1f}% | "
                f"{agg['mid_avg']:.1f}% | "
                f"{agg['low_avg']:.1f}% | "
                f"{agg['unique_total']} |\n"
            )
        # 附一段 footer 说明分组规则, 让表格本身可读、可投稿
        f.write(f"\n> 难度分组: 高约束 = fuzz4all.txt 的前 {HIGH_END} 个 API; "
                f"中约束 = 第 {HIGH_END+1}–{MID_END}; 低约束 = 第 {MID_END+1}–末尾。\n")
        f.write("> 平均有效率 = 各 API "
                "(filter+success 通过样本数 / 总采样数) 的算术平均。\n")
        f.write("> 唯一程序数 = 各 API 在该变体下 valid 程序经 ast unparse "
                "归一化后去重数量, 跨 API 求和。\n")

    print(f"[ablation] wrote summary to {md_path}", flush=True)


# =============================================================================
#                              中断保护 (SIGINT/SIGTERM)
# =============================================================================
# 长任务里随时可能被 ctrl-C 或 OOM-kill, 这里保证已跑完的 (variant, api)
# 都已经独立落盘 stats.json, 不会因为整体退出而丢失。

_GLOBAL_SUMMARY: Dict[str, Dict] = {}
_GLOBAL_OUT_DIR: Optional[str] = None


def _install_signal_handlers() -> None:
    def _h(signum, frame):
        print(f"\n[ablation] caught signal {signum}; "
              f"flushing partial summary and exiting.", flush=True)
        if _GLOBAL_OUT_DIR is not None and _GLOBAL_SUMMARY:
            try:
                write_summary(_GLOBAL_SUMMARY, _GLOBAL_OUT_DIR)
            except Exception as e:
                print(f"[ablation] flush failed: {e}", flush=True)
        sys.exit(128 + signum)
    signal.signal(signal.SIGINT, _h)
    signal.signal(signal.SIGTERM, _h)


# =============================================================================
#                                  主流程
# =============================================================================

def variant_prompts_for_api(
    api: str, variant: str,
    constraints_dir: str,
    separator: str, begin: str,
) -> Optional[str]:
    """根据变体拼出 user prompt。返回 None 表示该变体在该 API 上缺必要文件,
    应当跳过 (例如 B/C 没有 greedy_prompt.txt)。"""
    if variant == "A":
        _, user = build_prompt_A(api, separator, begin)
        return user

    greedy_path = os.path.join(constraints_dir, api,
                               "prompts", "greedy_prompt.txt")
    greedy_text = read_text_or_none(greedy_path)
    if greedy_text is None:
        # B 和 C 都依赖 greedy_prompt, 缺失就跳过
        return None

    if variant == "B":
        _, user = build_prompt_B(api, greedy_text, separator, begin)
        return user

    # variant == "C"
    struct_path = os.path.join(constraints_dir, api,
                               "prompts", "structured_info.txt")
    struct_text = read_text_or_none(struct_path)
    if struct_text is None:
        return None
    _, user = build_prompt_C(api, struct_text, greedy_text, separator, begin)
    return user


def main():
    parser = argparse.ArgumentParser(
        description="Prompt input ablation runner (no-doc / hw / auto-prompt) "
                    "using local Qwen2.5-Coder-7B-Instruct."
    )
    parser.add_argument("--apilist", type=str, default="data/fuzz4all.txt",
                        help="API 列表; 一行一个; 前 35 高约束, 36-70 中, 71-100 低。")
    parser.add_argument("--constraints_dir", type=str, default="experiment/torch",
                        help="结构化提示根目录, 期望 <constraints_dir>/<api>/"
                             "prompts/{greedy_prompt.txt,structured_info.txt}。")
    parser.add_argument("--out_dir", type=str, required=True,
                        help="实验输出根目录。会建 <out_dir>/<variant>/<api>/ "
                             "子目录, 以及顶层 summary.{json,csv,md}。")
    parser.add_argument("--model_path", type=str,
                        default="../Qwen2.5-Coder-7B-Instruct")
    parser.add_argument("--dtype", type=str, default="bfloat16",
                        choices=["bfloat16", "float16", "float32"])
    parser.add_argument("--library", type=str, default="torch",
                        choices=["torch", "tf"])
    parser.add_argument("--n_samples", type=int, default=30,
                        help="每 (api, variant) 采样数, 论文要求 30。")
    parser.add_argument("--temperature", type=float, default=0.4)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--validate_timeout", type=int,
                        default=DEFAULT_VALIDATE_TIMEOUT)
    parser.add_argument("--variants", type=str, default="A,B,C",
                        help="只跑指定变体的子集, 如 'A,C' 跳过 B。")
    parser.add_argument("--separator", type=str, default=DEFAULT_SEPARATOR)
    parser.add_argument("--begin", type=str, default=DEFAULT_BEGIN)
    parser.add_argument("--limit", type=int, default=None,
                        help="只处理 apilist 前 N 个 API (debug 用)。")
    parser.add_argument("--force_redo", action="store_true",
                        help="忽略已有 stats.json, 强制重跑。")
    args = parser.parse_args()

    apis = load_apis(args.apilist)
    if args.limit is not None:
        apis = apis[:args.limit]
    print(f"[ablation] loaded {len(apis)} APIs from {args.apilist}", flush=True)

    selected = [v.strip() for v in args.variants.split(",") if v.strip()]
    for v in selected:
        assert v in ("A", "B", "C"), f"unknown variant: {v}"

    os.makedirs(args.out_dir, exist_ok=True)

    # 暴露给信号处理器
    global _GLOBAL_OUT_DIR, _GLOBAL_SUMMARY
    _GLOBAL_OUT_DIR = args.out_dir
    _install_signal_handlers()

    load_qwen(args.model_path, args.dtype)

    # 主循环: 外层变体, 内层 API。这样跑就算中途 kill 也至少能拿到完整的
    # 头几个变体的全量结果, 不会被打散到三个变体都半成品。
    summary: Dict[str, Dict] = {}
    _GLOBAL_SUMMARY = summary

    for variant in selected:
        print(f"\n========== Variant {variant} ({VARIANT_LABELS[variant]}) "
              f"==========", flush=True)
        v_out = os.path.join(args.out_dir, variant)
        os.makedirs(v_out, exist_ok=True)

        per_api: List[Dict] = []
        n_skipped_missing_files = 0

        for idx, api in enumerate(apis):
            diff = difficulty_of(idx)
            api_dir = os.path.join(v_out, api)

            # --- 断点续跑: stats.json 已存在就直接复用 ---
            stats_path = os.path.join(api_dir, "stats.json")
            if (not args.force_redo) and os.path.isfile(stats_path):
                try:
                    with open(stats_path, "r", encoding="utf-8") as f:
                        cached = json.load(f)
                    cached["difficulty"] = diff
                    per_api.append(cached)
                    print(f"[ablation] [{variant}/{api}] "
                          f"({idx+1}/{len(apis)}, {diff}) resumed from cache "
                          f"(valid={cached.get('n_valid', '?')})",
                          flush=True)
                    continue
                except Exception:
                    pass  # 缓存坏了就重跑

            # --- 拼 prompt; 缺失文档的 B/C 直接跳过 ---
            user_prompt = variant_prompts_for_api(
                api, variant, args.constraints_dir,
                args.separator, args.begin,
            )
            if user_prompt is None:
                n_skipped_missing_files += 1
                print(f"[ablation] [{variant}/{api}] "
                      f"missing prompt files, skip.", flush=True)
                # 仍然记录一行, n_valid=0, 让该 API 进入分母
                # (否则 B/C 的"平均有效率"会被有利地高估)
                placeholder = {
                    "api": api, "variant": variant,
                    "n_samples_requested": args.n_samples,
                    "n_samples_received": 0, "n_filtered": 0,
                    "n_valid": 0, "n_unique_valid": 0,
                    "validity_rate": 0.0, "filter_rate": 0.0,
                    "status_breakdown": {"success": 0, "exception": 0,
                                         "crash": 0, "timeout": 0},
                    "gen_time_sec": 0.0,
                    "skipped_reason": "missing_prompt_files",
                    "difficulty": diff,
                }
                os.makedirs(api_dir, exist_ok=True)
                with open(stats_path, "w", encoding="utf-8") as f:
                    json.dump(placeholder, f, indent=2, ensure_ascii=False)
                per_api.append(placeholder)
                continue

            # --- 真正跑 ---
            print(f"[ablation] [{variant}/{api}] "
                  f"({idx+1}/{len(apis)}, {diff}) generating ...",
                  flush=True)
            try:
                stats = bench_one(
                    api=api, variant=variant,
                    prompt_user=user_prompt, library=args.library,
                    n_samples=args.n_samples,
                    temperature=args.temperature, top_p=args.top_p,
                    validate_timeout=args.validate_timeout,
                    save_dir=api_dir,
                )
            except Exception as e:
                print(f"[ablation] [{variant}/{api}] FAILED: {e}", flush=True)
                traceback.print_exc()
                stats = {
                    "api": api, "variant": variant,
                    "n_samples_requested": args.n_samples,
                    "n_samples_received": 0, "n_filtered": 0,
                    "n_valid": 0, "n_unique_valid": 0,
                    "validity_rate": 0.0, "filter_rate": 0.0,
                    "status_breakdown": {"success": 0, "exception": 0,
                                         "crash": 0, "timeout": 0},
                    "gen_time_sec": 0.0,
                    "error": str(e),
                }
                with open(stats_path, "w", encoding="utf-8") as f:
                    json.dump(stats, f, indent=2, ensure_ascii=False)

            stats["difficulty"] = diff
            per_api.append(stats)
            print(f"[ablation] [{variant}/{api}] "
                  f"valid={stats.get('n_valid', 0)}/"
                  f"{stats.get('n_samples_received', 0)} "
                  f"unique={stats.get('n_unique_valid', 0)} "
                  f"({stats.get('validity_rate', 0)*100:.1f}%)",
                  flush=True)

            # --- 每完成一个 API 就刷一次顶层 summary, 防止整 run 崩了空手而归 ---
            agg_now = aggregate(per_api)
            summary[variant] = {"per_api": per_api, "aggregate": agg_now}
            try:
                write_summary(summary, args.out_dir)
            except Exception as e:
                print(f"[ablation] WARN: flush summary failed: {e}",
                      flush=True)

            # 每个 API 之间清一次 cache, 避免长 run 显存碎片化
            try:
                import torch
                torch.cuda.empty_cache()
            except Exception:
                pass

        agg = aggregate(per_api)
        summary[variant] = {"per_api": per_api, "aggregate": agg}
        print(f"\n[ablation] [variant {variant}] DONE. "
              f"avg={agg['avg']:.1f}%, high={agg['high_avg']:.1f}%, "
              f"mid={agg['mid_avg']:.1f}%, low={agg['low_avg']:.1f}%, "
              f"unique={agg['unique_total']} "
              f"(skipped {n_skipped_missing_files} APIs for missing files)",
              flush=True)

    write_summary(summary, args.out_dir)
    print(f"\n[ablation] all done. See {args.out_dir}/summary.md", flush=True)


if __name__ == "__main__":
    main()