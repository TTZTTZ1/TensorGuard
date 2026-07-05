import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.demo_metrics import (  # noqa: E402
    append_metric,
    read_metrics,
    snapshot_qwen,
    snapshot_results,
)


def test_snapshot_counts_job_results():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "valid").mkdir()
        (root / "valid" / "torch.add_1.py").write_text("pass", encoding="utf-8")
        sample = snapshot_results(root)
        assert sample["valid"] == 1
        assert sample["crash"] == 0
        assert sample["total_files"] == 1


def test_snapshot_counts_driver_trace_evidence():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        root.mkdir(exist_ok=True)
        (root / "trace.txt").write_text("ok\nComparisonFail output mismatch\nINTERNAL ASSERT FAILED\n", encoding="utf-8")
        sample = snapshot_results(root)
        assert sample["trace_hits"] == 2


def test_snapshot_counts_completed_driver_testcases():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "trace.txt").write_text(
            "Results/torch 3\n"
            "Testcase 0 torch.add torch.add_1 NoProblem 420\n"
            "diagnostic output\n"
            "Testcase 1 torch.add torch.add_2 ComparisonFail 420\n"
            "Testcase malformed\n",
            encoding="utf-8",
        )
        sample = snapshot_results(root)
        assert sample["tested_cases"] == 2


def test_snapshot_qwen_counts_raw_and_fixed_programs():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "raw" / "torch.add").mkdir(parents=True)
        (root / "fix" / "torch.add").mkdir(parents=True)
        (root / "raw" / "torch.add" / "1.py").write_text("raw", encoding="utf-8")
        (root / "raw" / "torch.add" / "2.py").write_text("raw", encoding="utf-8")
        (root / "fix" / "torch.add" / "1.py").write_text("fixed", encoding="utf-8")
        assert snapshot_qwen(root, "torch.add") == {"qwen_raw": 2, "qwen_valid": 1}


def test_append_metric_writes_one_json_object_per_line():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "metrics.jsonl"
        append_metric(path, {"stage": "ev_generation", "valid": 1})
        append_metric(path, {"stage": "ev_generation", "valid": 2})
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        assert [row["valid"] for row in rows] == [1, 2]
        assert all("timestamp" in row for row in rows)
        assert read_metrics(path) == rows


if __name__ == "__main__":
    test_snapshot_counts_job_results()
    test_snapshot_counts_driver_trace_evidence()
    test_snapshot_counts_completed_driver_testcases()
    test_snapshot_qwen_counts_raw_and_fixed_programs()
    test_append_metric_writes_one_json_object_per_line()
    print("ok")
