"""
check_constraints.py — 在跑 Qwen 采样之前，对 DeepSeek 蒸馏出来的约束文件
做一次 schema 检查。Prompt 里拼进去的 YAML 必须结构一致，否则 Qwen 生成
质量会显著下滑。

用法:
    python check_constraints.py --constraints_dir constraints \\
                                --apilist data/torch_apis.txt \\
                                [--library torch]

出参:
    - 打印每个 API 的检查结果
    - 对缺失 / 错误的 YAML 写一份报告: <constraints_dir>/_lint_report.json
    - 退出码: 0 全部通过; 1 有任何 API 失败
"""

import argparse
import json
import os
import sys
import re
from typing import Any, Dict, List, Tuple

import yaml


REQUIRED_PARAM_KEYS = {"dtype", "range", "structure", "shape", "default"}

# DeepSeek 在"API 文档没提到某字段"时会填入这个字符串字面量占位。
# lint 时把它视为合法值 (既不算 list 也不算 null)。
NO_MENTION = "No mention"

# constraints 是 dict 形式 (如 {1: {...}, 2: {...}}) 时, 每一条约束必须
# 完整满足这三个键, 缺任何一个都 malformed。
CONSTRAINT_ITEM_REQUIRED_KEYS = {"Parameter 1", "Parameter 2", "Constraint"}


def _is_list_or_none_or_nomention(v: Any) -> bool:
    """
    严格口径: 接受 None, list, 或 *严格等于* 字符串 "No mention"。
    其他任何字符串 (比如写成了 "float" 而不是 ["float"]) 一律 malformed。
    """
    if v is None or isinstance(v, list):
        return True
    if isinstance(v, str) and v == NO_MENTION:
        return True
    return False


def _fix_yaml_with_special_keys(content: str) -> str:
    """
    将 YAML 内容中的特殊键名和值中的别名引用（*identifier）替换为带引号的形式，
    避免被 PyYAML 解析为未定义锚点。
    处理场景：
      1. 键名: 行首或缩进后的 *args: 或 **kwargs:  ->  '*args':  /  '**kwargs':
      2. 值中的别名引用: 冒号+空格后的 *identifier  ->  ': '*identifier''
         (例如 Parameter 2: *args, params: *tensors, constraints: *some_alias)
    """
    # 1. 处理特殊键名: *args: 或 **kwargs:
    def repl_key(match):
        indent = match.group(1)
        key = match.group(2)
        colon = match.group(3)
        return f"{indent}'{key}'{colon}"

    pattern_key = re.compile(r'^(\s*)(\*args|\*\*kwargs)(:)', re.MULTILINE)
    content = pattern_key.sub(repl_key, content)

    # 2. 处理值中的别名引用: 匹配 : 空格或制表符后跟 *identifier
    # 其中 identifier 以字母或下划线开头，后跟字母数字下划线
    def repl_alias(match):
        prefix = match.group(1)   # 包括冒号和后面的空白
        alias = match.group(2)    # *identifier
        return f"{prefix}'{alias}'"

    pattern_val = re.compile(r'(:\s+)(\*[a-zA-Z_][a-zA-Z0-9_]*)')
    content = pattern_val.sub(repl_alias, content)

    return content


def lint_one(path: str) -> Tuple[bool, List[str], int]:
    """
    检查单个约束文件。返回 (ok, issues, no_mention_count).

    no_mention_count: 该文件内字段值为 "No mention" 的出现次数, 用于统计
    DeepSeek 对该 API 的覆盖度 (数值越高说明约束越稀疏, Qwen 生成时的引
    导信息越少)。
    """
    issues: List[str] = []
    no_mention = 0

    if not os.path.isfile(path):
        return False, [f"file not found: {path}"], 0

    try:
        with open(path, "r") as f:
            raw_content = f.read()
        # 修复 *args / **kwargs 键名
        fixed_content = _fix_yaml_with_special_keys(raw_content)
        data = yaml.safe_load(fixed_content)
    except Exception as e:
        return False, [f"YAML parse error: {e}"], 0

    if not isinstance(data, dict):
        return False, [f"top-level must be a mapping, got {type(data).__name__}"], 0

    # `constraints`: 允许 null / str / list / dict
    #   - null            : 无跨参数约束 (常见)
    #   - str             : 自由文本说明 (如 "No constraints specified...")
    #   - list            : 结构化约束列表
    #   - dict (编号作键) : 例
    #         1:
    #           Parameter 1: "target"
    #           Parameter 2: "source"
    #           Constraint: "target.shape[0] == source.shape[0]"
    #       对 dict 形式做严格子校验: 每一条必须含
    #       'Parameter 1' / 'Parameter 2' / 'Constraint' 三键。
    if "constraints" not in data:
        issues.append("missing top-level key: constraints")
    else:
        cdata = data["constraints"]
        if cdata is None or isinstance(cdata, (str, list)):
            pass  # 接受
        elif isinstance(cdata, dict):
            for key, item in cdata.items():
                loc = f"constraints[{key!r}]"
                if not isinstance(item, dict):
                    issues.append(f"{loc}: must be a mapping, got "
                                  f"{type(item).__name__}")
                    continue
                missing = CONSTRAINT_ITEM_REQUIRED_KEYS - set(item.keys())
                if missing:
                    issues.append(f"{loc}: missing keys {sorted(missing)}")
        else:
            issues.append(f"constraints should be null/str/list/dict, got "
                          f"{type(cdata).__name__}")

    # `params` 可以是 dict 或 None（表示无参数）
    params = data.get("params")
    if params is None:
        # 无参数，合法，跳过后续检查
        return len(issues) == 0, issues, 0

    if not isinstance(params, dict):
        issues.append("`params` must be a mapping or null, "
                      f"got {type(params).__name__}")
        return len(issues) == 0, issues, no_mention

    if len(params) == 0:
        # 空字典也视为有效（无参数），不报错
        # 但可以保留一条 info，不过按原逻辑不当作 issue
        pass

    for pname, pspec in params.items():
        if not isinstance(pspec, dict):
            issues.append(f"param {pname!r}: spec must be a mapping")
            continue
        missing = REQUIRED_PARAM_KEYS - set(pspec.keys())
        if missing:
            issues.append(f"param {pname!r}: missing keys {sorted(missing)}")

        # 统计 "No mention" 出现次数 (每个字段都可能被标记)
        for k in ("dtype", "range", "structure", "shape", "default"):
            if pspec.get(k) == NO_MENTION:
                no_mention += 1

        # dtype / structure / shape / range: 严格——list / null / "No mention"
        # (严禁写成裸字符串 "float"、"tensor" 等; 若需要字面量必须包 list)
        for k in ("dtype", "structure", "shape", "range"):
            if k in pspec and not _is_list_or_none_or_nomention(pspec[k]):
                got = pspec[k]
                got_desc = repr(got) if isinstance(got, str) else type(got).__name__
                issues.append(
                    f"param {pname!r}: {k} must be list/null/'No mention', "
                    f"got {got_desc}"
                )

    return len(issues) == 0, issues, no_mention


CONSTRAINT_FILENAME = "structured_info.txt"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--constraints_dir", required=True,
                        help="Root of DeepSeek-distilled constraints. "
                             "Expected layout: "
                             "<constraints_dir>/<api>/structured_info.txt")
    parser.add_argument("--apilist", default=None,
                        help="newline-separated API list; if omitted, lint "
                             "every subdirectory under constraints_dir that "
                             "contains a structured_info.txt")
    parser.add_argument("--library", default=None,
                        choices=["torch", "tf"],
                        help="only used for report tagging")
    args = parser.parse_args()

    if args.apilist:
        with open(args.apilist, "r") as f:
            apis = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        paths = [(api, os.path.join(args.constraints_dir, api, "prompts", CONSTRAINT_FILENAME))
                 for api in apis]
    else:
        # 扫 constraints_dir 下每个子目录
        paths = []
        if os.path.isdir(args.constraints_dir):
            for name in sorted(os.listdir(args.constraints_dir)):
                sub = os.path.join(args.constraints_dir, name)
                if not os.path.isdir(sub):
                    continue
                info_path = os.path.join(sub, CONSTRAINT_FILENAME)
                # 即使文件不存在也放进来，下面 lint_one 会报 missing
                paths.append((name, info_path))

    report: Dict[str, Any] = {
        "library": args.library,
        "total": len(paths),
        "ok": 0,
        "missing": 0,
        "malformed": 0,
        "total_no_mention_fields": 0,
        "top_sparse_apis": [],       # 约束最稀疏的前 N 个 API (按 no_mention 降序)
        "details": {},
    }

    per_api_no_mention: List[Tuple[str, int]] = []

    for api, p in paths:
        ok, issues, nm = lint_one(p)
        per_api_no_mention.append((api, nm))
        report["total_no_mention_fields"] += nm
        if ok:
            report["ok"] += 1
        elif issues and issues[0].startswith("file not found"):
            report["missing"] += 1
            report["details"][api] = issues
        else:
            report["malformed"] += 1
            report["details"][api] = issues

    # 给出 no_mention 最多的前 10 个 (帮助定位约束覆盖差的 API)
    per_api_no_mention.sort(key=lambda x: x[1], reverse=True)
    report["top_sparse_apis"] = [
        {"api": a, "no_mention_fields": n}
        for a, n in per_api_no_mention[:10] if n > 0
    ]

    out = os.path.join(args.constraints_dir, "_lint_report.json")
    with open(out, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Total:    {report['total']}")
    print(f"  OK:      {report['ok']}")
    print(f"  Missing: {report['missing']}")
    print(f"  Malformed: {report['malformed']}")
    print(f"'No mention' fields (sum): {report['total_no_mention_fields']}")
    if report["top_sparse_apis"]:
        print(f"Sparsest APIs (top {len(report['top_sparse_apis'])}):")
        for entry in report["top_sparse_apis"]:
            print(f"  {entry['api']:40s}  {entry['no_mention_fields']} fields")
    print(f"Report: {out}")

    # first few malformed examples for quick diagnosis
    bad = [(k, v) for k, v in report["details"].items()
           if not v[0].startswith("file not found")]
    for api, issues in bad[:5]:
        print(f"\n[{api}]")
        for issue in issues:
            print(f"  - {issue}")

    return 0 if report["malformed"] == 0 and report["missing"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())