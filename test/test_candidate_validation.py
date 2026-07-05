import json
import sys
import tempfile
import time
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def test_candidate_mode_uses_isolated_cpu_and_gpu_environments():
    from webapp.candidate_validation import run_candidate_mode

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        repro = root / "repro.py"
        repro.write_text(
            "import os\nprint('visible=' + os.environ.get('CUDA_VISIBLE_DEVICES', '<unset>'))\n",
            encoding="utf-8",
        )

        cpu = run_candidate_mode(repro, "cpu", root / "cpu.log", 5, python_executable=sys.executable)
        gpu = run_candidate_mode(repro, "gpu0", root / "gpu0.log", 5, python_executable=sys.executable)

        assert cpu["returncode"] == 0
        assert gpu["returncode"] == 0
        assert "visible=" in (root / "cpu.log").read_text(encoding="utf-8")
        assert "visible=0" in (root / "gpu0.log").read_text(encoding="utf-8")
        assert cpu["execution_profile"] == "cuda_hidden"
        assert gpu["execution_profile"] == "visible_gpu_0"


def test_candidate_mode_records_timeout():
    from webapp.candidate_validation import run_candidate_mode

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        repro = root / "repro.py"
        repro.write_text("import time\ntime.sleep(2)\n", encoding="utf-8")

        result = run_candidate_mode(repro, "cpu", root / "cpu.log", 1, python_executable=sys.executable)

        assert result["status"] == "timeout"
        assert result["timed_out"] is True
        assert result["evidence"]["outcome"] == "timeout"


def test_execute_candidate_validation_writes_structured_status_and_logs():
    from webapp.candidate_validation import execute_candidate_validation

    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "run"
        out.mkdir()
        repro = out / "repro.py"
        repro.write_text("print('candidate validation')\n", encoding="utf-8")

        status = execute_candidate_validation(
            out,
            {"run_id": "candidate_run_1", "cluster_id": "cluster_1", "timeout_seconds": 5},
            python_executable=sys.executable,
        )

        persisted = json.loads((out / "status.json").read_text(encoding="utf-8"))
        assert status["status"] == "finished"
        assert persisted["status"] == "finished"
        assert set(persisted["modes"]) == {"cpu", "gpu0"}
        assert (out / "cpu.log").is_file()
        assert (out / "gpu0.log").is_file()


def test_server_starts_and_polls_candidate_validation_job():
    from webapp import server
    from webapp.candidates import CandidateStore

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "demo_runs/api_jobs/job1/Results/torch/exception/torch.add_1.py"
        source.parent.mkdir(parents=True)
        source.write_text('"""INTERNAL ASSERT FAILED"""\nprint(\'candidate validation\')\n', encoding="utf-8")
        store = CandidateStore(root)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = store.list_clusters()[0]["cluster_id"]

        with patch.object(server, "CANDIDATE_STORE", store):
            code, started = server.start_candidate_validation(cluster_id, {"source": "print('saved run')\n", "timeout": 5})
            assert code == 202
            deadline = time.time() + 5
            while True:
                code, payload = server.candidate_validation_job_payload(started["run_id"])
                if payload.get("status") == "finished" or time.time() >= deadline:
                    break
                time.sleep(0.05)

        assert code == 200
        assert payload["status"] == "finished"
        assert "saved run" in payload["logs"]["cpu"]
        assert "saved run" in payload["logs"]["gpu0"]


if __name__ == "__main__":
    test_candidate_mode_uses_isolated_cpu_and_gpu_environments()
    test_candidate_mode_records_timeout()
    test_execute_candidate_validation_writes_structured_status_and_logs()
    test_server_starts_and_polls_candidate_validation_job()
    print("ok")
