import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.server import initial_api_status, list_job_result_files, unique_job_directory  # noqa: E402
from webapp import server  # noqa: E402


def test_job_result_files_are_scoped_to_selected_api():
    with tempfile.TemporaryDirectory() as tmp:
        job = Path(tmp)
        crash = job / "Results" / "torch" / "crash"
        crash.mkdir(parents=True)
        (crash / "torch.add_1.py").write_text("raise RuntimeError('boom')", encoding="utf-8")
        (crash / "torch.mean_1.py").write_text("pass", encoding="utf-8")

        files = list_job_result_files(job, "torch", "torch.add")

        assert len(files["crash"]) == 1
        assert files["crash"][0]["name"] == "torch.add_1.py"
        assert "boom" in files["crash"][0]["source_excerpt"]
        assert files["valid"] == []


def test_job_directory_never_reuses_existing_run():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "job").mkdir()
        job_id, path = unique_job_directory(root, "job")
        assert job_id == "job_2"
        assert path.is_dir()


def test_web_job_is_pending_before_child_process_starts():
    status = initial_api_status("job", "torch", "torch.add", "demo", "qwen", "incoder", "0")
    assert status["status"] == "pending"
    assert status["stages"]["prompt_check"] == "pending"
    assert status["mutation_model"] == "incoder"


def test_latest_repro_job_is_scoped_to_bug_and_uses_newest_status_file():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        fixtures = [
            ("old", "BUG-A", 100),
            ("new", "BUG-A", 300),
            ("other", "BUG-B", 400),
        ]
        for job_id, bug_id, modified in fixtures:
            status = root / job_id / "status.json"
            status.parent.mkdir()
            status.write_text(json.dumps({"job_id": job_id, "bug_id": bug_id, "status": "finished"}), encoding="utf-8")
            os.utime(status, (modified, modified))

        latest = server.latest_repro_summary_for_bug("BUG-A", root)

        assert latest is not None
        assert latest["job_id"] == "new"
        assert server.latest_repro_summary_for_bug("BUG-C", root) is None


def test_confirmed_bug_detail_includes_latest_repro_job_id():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        bug_dir = root / "reports" / "bug-a"
        bug_dir.mkdir(parents=True)
        meta = {"id": "BUG-A", "files": {"repro": "repro.py", "report": "report.md"}}
        meta_path = bug_dir / "meta.json"
        meta_path.write_text(json.dumps(meta), encoding="utf-8")
        (bug_dir / "repro.py").write_text("print('repro')", encoding="utf-8")
        repro_status = root / "demo_runs" / "repro_jobs" / "repro-new" / "status.json"
        repro_status.parent.mkdir(parents=True)
        repro_status.write_text(json.dumps({"job_id": "repro-new", "bug_id": "BUG-A", "status": "finished"}), encoding="utf-8")
        index_item = {"id": "BUG-A", "path": "reports/bug-a/meta.json", "display_id": "BUG-A"}

        with (
            patch.object(server, "REPO_ROOT", root),
            patch.object(server, "REPRO_JOB_ROOT", root / "demo_runs" / "repro_jobs"),
            patch.object(server, "load_paper_bugs", return_value=[index_item]),
        ):
            code, payload = server.paper_bug_detail("BUG-A")

        assert code == 200
        assert payload["latest_repro_job_id"] == "repro-new"


if __name__ == "__main__":
    test_job_result_files_are_scoped_to_selected_api()
    test_job_directory_never_reuses_existing_run()
    test_web_job_is_pending_before_child_process_starts()
    test_latest_repro_job_is_scoped_to_bug_and_uses_newest_status_file()
    test_confirmed_bug_detail_includes_latest_repro_job_id()
    print("ok")
