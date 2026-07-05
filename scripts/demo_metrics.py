"""Structured metrics for one-API demo jobs."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


RESULT_SUBDIRS = ("seed", "valid", "exception", "crash", "notarget", "hangs", "flaky")
TRACE_PATTERNS = ("Catch", "Fail", "INTERNAL ASSERT", "device-side assert", "Segmentation fault", "Floating point exception", "free()")


def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def count_py(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for child in path.iterdir() if child.is_file() and child.suffix == ".py")


def snapshot_results(root: Path) -> dict:
    counts = {name: count_py(root / name) for name in RESULT_SUBDIRS}
    counts["total_files"] = sum(counts.values())
    trace_path = root / "trace.txt"
    trace_hits = 0
    tested_case_ids: set[int] = set()
    if trace_path.is_file():
        with trace_path.open("r", encoding="utf-8", errors="replace") as stream:
            for line in stream:
                if any(pattern in line for pattern in TRACE_PATTERNS):
                    trace_hits += 1
                parts = line.split()
                if len(parts) >= 5 and parts[0] == "Testcase":
                    try:
                        tested_case_ids.add(int(parts[1]))
                    except ValueError:
                        pass
    counts["tested_cases"] = len(tested_case_ids)
    counts["trace_hits"] = trace_hits
    return counts


def snapshot_qwen(root: Path, api: str) -> dict:
    return {
        "qwen_raw": count_py(root / "raw" / api),
        "qwen_valid": count_py(root / "fix" / api),
    }


def append_metric(path: Path, metric: dict) -> dict:
    row = dict(metric)
    row.setdefault("timestamp", timestamp())
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        f.flush()
    return row


def read_metrics(path: Path, limit: Optional[int] = None) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict):
                rows.append(item)
    if limit is not None and limit >= 0:
        return rows[-limit:]
    return rows


def build_metric(
    stage: str,
    elapsed_seconds: float,
    qwen_root: Path,
    results_root: Path,
    api: str,
    gpu_sample: Optional[dict] = None,
) -> dict:
    metric = {
        "stage": stage,
        "elapsed_seconds": round(elapsed_seconds, 3),
        **snapshot_qwen(qwen_root, api),
        **snapshot_results(results_root),
    }
    if gpu_sample:
        metric["gpu"] = gpu_sample
    return metric
