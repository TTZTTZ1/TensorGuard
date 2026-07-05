#!/usr/bin/env python3
"""Validate the fixed prompt/constraint library used by the demo workbench."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


REQUIRED_PARAM_KEYS = {"dtype", "range", "structure", "shape", "default"}
SUPPORTED_LIBS = ("torch", "tf")


def load_manifest(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def try_load_yaml(text: str) -> Tuple[Optional[Any], Optional[str]]:
    try:
        import yaml  # type: ignore
    except Exception:
        return None, None

    try:
        return yaml.safe_load(text), None
    except Exception as exc:
        return None, f"YAML parse error: {exc}"


def validate_structured_text(text: str) -> Tuple[str, List[str]]:
    issues: List[str] = []
    if not text.strip():
        return "error", ["structured_info.txt is empty"]

    if "params:" not in text:
        issues.append("missing text marker: params:")
    if "constraints:" not in text:
        issues.append("missing text marker: constraints:")

    data, yaml_issue = try_load_yaml(text)
    if yaml_issue:
        issues.append(yaml_issue)
    elif data is not None:
        if not isinstance(data, dict):
            issues.append(f"top-level YAML must be a mapping, got {type(data).__name__}")
        else:
            if "constraints" not in data:
                issues.append("missing top-level key: constraints")
            params = data.get("params")
            if params is not None:
                if not isinstance(params, dict):
                    issues.append(f"params must be a mapping or null, got {type(params).__name__}")
                else:
                    for pname, spec in params.items():
                        if not isinstance(spec, dict):
                            issues.append(f"param {pname!r}: spec must be a mapping")
                            continue
                        missing = REQUIRED_PARAM_KEYS - set(spec.keys())
                        if missing:
                            issues.append(f"param {pname!r}: missing keys {sorted(missing)}")

    if any(i.startswith("YAML parse error") or "must be" in i for i in issues):
        return "error", issues
    if issues:
        return "warning", issues
    return "ok", []


def selected_entries(manifest: dict, lib: Optional[str], api: Optional[str]) -> List[Tuple[str, str, dict]]:
    libs: Dict[str, dict] = manifest.get("libraries", {})
    selected_libs = [lib] if lib else [name for name in SUPPORTED_LIBS if name in libs]
    entries: List[Tuple[str, str, dict]] = []
    for lib_name in selected_libs:
        lib_entries = libs.get(lib_name, {})
        if api:
            if api in lib_entries:
                entries.append((lib_name, api, lib_entries[api]))
            continue
        for api_name, entry in sorted(lib_entries.items()):
            entries.append((lib_name, api_name, entry))
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prompt library files.")
    parser.add_argument("--manifest", default="prompt_library_manifest.json")
    parser.add_argument("--root", default=".")
    parser.add_argument("--lib", choices=SUPPORTED_LIBS, default=None)
    parser.add_argument("--api", default=None)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path

    manifest = load_manifest(manifest_path)
    entries = selected_entries(manifest, args.lib, args.api)
    if args.api and not entries:
        print(f"ERROR {args.lib or '*'}:{args.api} not found in manifest")
        return 2

    counts = {"ok": 0, "warning": 0, "error": 0}
    errors: List[str] = []
    warnings: List[str] = []

    for lib, api, entry in entries:
        structured_rel = entry.get("structured_info")
        if not structured_rel:
            counts["error"] += 1
            errors.append(f"{lib}:{api}: missing structured_info path in manifest")
            continue
        structured_path = root / structured_rel
        if not structured_path.is_file():
            counts["error"] += 1
            errors.append(f"{lib}:{api}: file not found: {structured_rel}")
            continue

        text = structured_path.read_text(encoding="utf-8", errors="replace")
        status, issues = validate_structured_text(text)
        counts[status] += 1
        if status == "error":
            errors.append(f"{lib}:{api}: {'; '.join(issues)}")
        elif status == "warning":
            warnings.append(f"{lib}:{api}: {'; '.join(issues)}")

    total = sum(counts.values())
    if args.api and total == 1:
        lib, api, _ = entries[0]
        if counts["ok"] == 1:
            print(f"OK {api}")
            return 0
        for line in errors + warnings:
            print(line)
        return 1 if errors else 0

    print("Prompt library validation")
    print(f"total:   {total}")
    print(f"ok:      {counts['ok']}")
    print(f"warning: {counts['warning']}")
    print(f"error:   {counts['error']}")

    for line in errors[:20]:
        print("ERROR", line)
    for line in warnings[:20]:
        print("WARNING", line)
    if len(errors) > 20:
        print(f"... {len(errors) - 20} more errors")
    if len(warnings) > 20:
        print(f"... {len(warnings) - 20} more warnings")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
