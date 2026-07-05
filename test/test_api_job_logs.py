import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp import server  # noqa: E402


def test_api_job_log_chunk_reads_whitelisted_log_incrementally():
    with tempfile.TemporaryDirectory() as tmp:
        jobs_root = Path(tmp) / "api_jobs"
        log_dir = jobs_root / "job-1" / "logs"
        log_dir.mkdir(parents=True)
        (log_dir / "01_qwen_seed.log").write_bytes(b"first\nsecond\n")

        with patch.object(server, "API_JOB_ROOT", jobs_root), patch.object(server, "LOG_CHUNK_BYTES", 6, create=True):
            code, first = server.api_job_log_chunk("job-1", "01_qwen_seed.log", 0)
            code_2, second = server.api_job_log_chunk("job-1", "01_qwen_seed.log", first["next_offset"])

        assert code == 200
        assert first == {
            "job_id": "job-1",
            "log_name": "01_qwen_seed.log",
            "text": "first\n",
            "offset": 0,
            "next_offset": 6,
            "size_bytes": 13,
            "has_more": True,
            "reset": False,
        }
        assert code_2 == 200
        assert second["text"] == "second"
        assert second["offset"] == 6
        assert second["next_offset"] == 12
        assert second["has_more"] is True


def test_api_job_log_chunk_resets_after_file_truncation():
    with tempfile.TemporaryDirectory() as tmp:
        jobs_root = Path(tmp) / "api_jobs"
        log_dir = jobs_root / "job-1" / "logs"
        log_dir.mkdir(parents=True)
        (log_dir / "02_ev_generation.log").write_text("new\n", encoding="utf-8")

        with patch.object(server, "API_JOB_ROOT", jobs_root):
            code, payload = server.api_job_log_chunk("job-1", "02_ev_generation.log", 999)

        assert code == 200
        assert payload["reset"] is True
        assert payload["offset"] == 0
        assert payload["text"] == "new\n"
        assert payload["next_offset"] == 4


def test_api_job_log_chunk_does_not_split_utf8_characters():
    with tempfile.TemporaryDirectory() as tmp:
        jobs_root = Path(tmp) / "api_jobs"
        log_dir = jobs_root / "job-1" / "logs"
        log_dir.mkdir(parents=True)
        (log_dir / "03_driver.log").write_text("状态正常\n", encoding="utf-8")

        with patch.object(server, "API_JOB_ROOT", jobs_root), patch.object(server, "LOG_CHUNK_BYTES", 5):
            _, first = server.api_job_log_chunk("job-1", "03_driver.log", 0)
            _, second = server.api_job_log_chunk("job-1", "03_driver.log", first["next_offset"])
            _, third = server.api_job_log_chunk("job-1", "03_driver.log", second["next_offset"])
            _, fourth = server.api_job_log_chunk("job-1", "03_driver.log", third["next_offset"])

        combined = first["text"] + second["text"] + third["text"] + fourth["text"]
        assert "�" not in combined
        assert combined == "状态正常\n"
        assert first["next_offset"] == 3
        assert second["next_offset"] == 6
        assert third["next_offset"] == 9
        assert fourth["next_offset"] == 13


def test_api_job_log_chunk_handles_missing_file_and_rejects_unknown_name():
    with tempfile.TemporaryDirectory() as tmp:
        jobs_root = Path(tmp) / "api_jobs"
        (jobs_root / "job-1").mkdir(parents=True)

        with patch.object(server, "API_JOB_ROOT", jobs_root):
            code, missing = server.api_job_log_chunk("job-1", "03_driver.log", 0)
            bad_code, bad = server.api_job_log_chunk("job-1", "../status.json", 0)

        assert code == 200
        assert missing["text"] == ""
        assert missing["next_offset"] == 0
        assert missing["has_more"] is False
        assert bad_code == 400
        assert bad["error"] == "unsupported API job log"


if __name__ == "__main__":
    test_api_job_log_chunk_reads_whitelisted_log_incrementally()
    test_api_job_log_chunk_resets_after_file_truncation()
    test_api_job_log_chunk_does_not_split_utf8_characters()
    test_api_job_log_chunk_handles_missing_file_and_rejects_unknown_name()
    print("ok")
