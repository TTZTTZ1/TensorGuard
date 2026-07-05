#!/usr/bin/env python3
"""Build an index for the fixed prompt/constraint library.

The demo workbench treats DeepSeek output as an offline artifact. This script
indexes files under experiment/<lib>/<api>/prompts so runtime code can look up
API constraints without scanning the whole tree each time.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
from pathlib import Path
from typing import Dict, Optional


SUPPORTED_LIBS = ("torch", "tf")
STRUCTURED_NAME = "structured_info.txt"
GREEDY_NAME = "greedy_prompt.txt"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Optional[Path], root: Path) -> Optional[str]:
    if path is None:
        return None
    return path.relative_to(root).as_posix()


def index_library(root: Path, lib: str) -> Dict[str, dict]:
    lib_root = root / "experiment" / lib
    entries: Dict[str, dict] = {}
    if not lib_root.is_dir():
        return entries

    for api_dir in sorted(p for p in lib_root.iterdir() if p.is_dir()):
        prompts_dir = api_dir / "prompts"
        structured = prompts_dir / STRUCTURED_NAME
        if not structured.is_file():
            continue

        greedy = prompts_dir / GREEDY_NAME
        greedy_path = greedy if greedy.is_file() else None
        updated_ts = max(
            structured.stat().st_mtime,
            greedy_path.stat().st_mtime if greedy_path else structured.stat().st_mtime,
        )
        updated_at = _dt.datetime.fromtimestamp(updated_ts).isoformat(timespec="seconds")

        api = api_dir.name
        entries[api] = {
            "api": api,
            "library": lib,
            "structured_info": rel(structured, root),
            "greedy_prompt": rel(greedy_path, root),
            "has_greedy_prompt": greedy_path is not None,
            "structured_sha256": sha256_file(structured),
            "greedy_sha256": sha256_file(greedy_path) if greedy_path else None,
            "updated_at": updated_at,
        }

    return entries


def build_manifest(root: Path) -> dict:
    libs = {lib: index_library(root, lib) for lib in SUPPORTED_LIBS}
    total = sum(len(v) for v in libs.values())
    return {
        "version": _dt.date.today().isoformat(),
        "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "total_apis": total,
        "libraries": libs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Index the fixed prompt library.")
    parser.add_argument(
        "--root",
        default=".",
        help="TensorGuard root directory. Defaults to current directory.",
    )
    parser.add_argument(
        "--out",
        default="prompt_library_manifest.json",
        help="Manifest output path relative to root unless absolute.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.out)
    if not out.is_absolute():
        out = root / out

    manifest = build_manifest(root)
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"manifest: {out}")
    for lib in SUPPORTED_LIBS:
        print(f"{lib}: {len(manifest['libraries'][lib])}")
    print(f"total: {manifest['total_apis']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
