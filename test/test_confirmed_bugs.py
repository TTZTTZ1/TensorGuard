import json
import hashlib
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.confirmed_bugs import DynamicConfirmedBugStore, load_confirmed_records  # noqa: E402
from webapp.candidates import CandidateStore  # noqa: E402
from webapp import server  # noqa: E402


def test_confirmed_index_excludes_entries_without_repro_source():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        good = root / "good"
        bad = root / "bad"
        good.mkdir()
        bad.mkdir()
        (good / "repro.py").write_text("print('ok')", encoding="utf-8")
        (good / "meta.json").write_text(json.dumps({"id": "BUG-1", "files": {"repro": "repro.py"}}), encoding="utf-8")
        (bad / "meta.json").write_text(json.dumps({"id": "BUG-2", "files": {"repro": "missing.py"}}), encoding="utf-8")
        index = root / "index.json"
        index.write_text(json.dumps([
            {"id": "BUG-1", "path": "good/meta.json", "severity": "High"},
            {"id": "BUG-2", "path": "bad/meta.json", "severity": "High"},
        ]), encoding="utf-8")

        records = load_confirmed_records(index, root)

        assert [record["id"] for record in records] == ["BUG-1"]
        assert "severity" not in records[0]


def test_dynamic_confirmed_store_archives_evidence_and_requires_id_to_delete():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        repro = root / "candidate-repro.py"
        repro.write_text("print('repro')\n", encoding="utf-8")
        validation = root / "validation"
        validation.mkdir()
        (validation / "cpu.log").write_text("CPU evidence\n", encoding="utf-8")
        (validation / "gpu0.log").write_text("GPU evidence\n", encoding="utf-8")
        status = {
            "run_id": "run-1",
            "status": "finished",
            "modes": {"cpu": {"returncode": 0}, "gpu0": {"returncode": 1}},
        }
        (validation / "status.json").write_text(json.dumps(status), encoding="utf-8")
        store = DynamicConfirmedBugStore(root)

        record = store.archive_candidate(
            cluster={
                "cluster_id": "cluster-1",
                "lib": "torch",
                "api": "torch.add",
                "category": "exception",
                "bug_pattern": "CPU/GPU value inconsistency",
            },
            repro_path=repro,
            validation_dir=validation,
            environment={"python": {"version": "3.10"}},
            review_metadata={
                "title": "torch.add CPU/GPU 结果不一致",
                "bug_type": "CPU/GPU value mismatch",
                "review_note": "独立复现后，CPU 与 GPU 返回值稳定不一致。",
            },
        )

        assert record["id"] == "BUG-0001"
        assert record["dynamic"] is True
        assert record["title"] == "torch.add CPU/GPU 结果不一致"
        assert record["bug_type"] == "CPU/GPU value mismatch"
        assert record["review_note"] == "独立复现后，CPU 与 GPU 返回值稳定不一致。"
        bug_dir = root / record["path"].replace("meta.json", "")
        assert (bug_dir / "repro.py").read_text(encoding="utf-8") == "print('repro')\n"
        assert (bug_dir / "evidence/cpu.log").read_text(encoding="utf-8") == "CPU evidence\n"
        assert (bug_dir / "environment.json").is_file()
        assert load_confirmed_records(store.index_path, root)[0]["id"] == "BUG-0001"

        try:
            store.delete("BUG-0001", confirmation_id="BUG-9999")
        except ValueError:
            pass
        else:
            raise AssertionError("wrong confirmation id must not delete a confirmed bug")
        assert store.get("BUG-0001") is not None

        store.delete("BUG-0001", confirmation_id="BUG-0001")
        assert store.get("BUG-0001") is None
        assert not bug_dir.exists()


def test_server_confirms_validated_candidate_and_deletes_dynamic_bug_by_id():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "demo_runs/api_jobs/job1/Results/torch/exception/torch.add_1.py"
        source.parent.mkdir(parents=True)
        source.write_text('"""INTERNAL ASSERT FAILED"""\nprint(\'candidate\')\n', encoding="utf-8")
        candidates = CandidateStore(root)
        candidates.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = candidates.list_clusters()[0]["cluster_id"]
        repro_source = "print('minimal repro')\n"
        candidates.save_cluster_draft(cluster_id, repro_source)
        run_dir = candidates.cluster_workspace_path(cluster_id) / "runs" / "run-1"
        run_dir.mkdir(parents=True)
        (run_dir / "status.json").write_text(
            json.dumps({
                "run_id": "run-1",
                "cluster_id": cluster_id,
                "status": "finished",
                "source_sha256": hashlib.sha256(repro_source.encode("utf-8")).hexdigest(),
                "modes": {},
            }),
            encoding="utf-8",
        )
        (run_dir / "cpu.log").write_text("CPU evidence\n", encoding="utf-8")
        (run_dir / "gpu0.log").write_text("GPU evidence\n", encoding="utf-8")
        confirmed = DynamicConfirmedBugStore(root)

        with (
            patch.object(server, "REPO_ROOT", root),
            patch.object(server, "CANDIDATE_STORE", candidates),
            patch.object(server, "DYNAMIC_CONFIRMED_STORE", confirmed),
            patch.object(server, "environment_payload", return_value={"python": {"version": "3.10"}}),
        ):
            code, detail = server.confirm_candidate_cluster(cluster_id, {
                "title": "torch.add 内部断言失败",
                "bug_type": "Internal assertion failure",
                "review_note": "CPU/GPU 独立进程复现完成，确认是框架内部断言。",
            })
            assert code == 201
            bug_id = detail["meta"]["id"]
            assert bug_id == "BUG-0001"
            assert detail["meta"]["title"] == "torch.add 内部断言失败"
            assert detail["meta"]["bug_type"] == "Internal assertion failure"
            assert detail["meta"]["review_note"] == "CPU/GPU 独立进程复现完成，确认是框架内部断言。"
            assert candidates.list_clusters() == []

            code, error = server.delete_confirmed_bug(bug_id, {"confirmation_id": "wrong"})
            assert code == 400
            assert confirmed.get(bug_id) is not None

            code, deleted = server.delete_confirmed_bug(bug_id, {"confirmation_id": bug_id})
            assert code == 200
            assert deleted["deleted"] == bug_id
            assert confirmed.get(bug_id) is None


def test_server_rejects_confirmation_when_saved_draft_changed_after_validation():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "demo_runs/api_jobs/job1/Results/torch/exception/torch.add_1.py"
        source.parent.mkdir(parents=True)
        source.write_text('"""INTERNAL ASSERT FAILED"""\nprint(\'candidate\')\n', encoding="utf-8")
        candidates = CandidateStore(root)
        candidates.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = candidates.list_clusters()[0]["cluster_id"]
        validated_source = "print('validated repro')\n"
        candidates.save_cluster_draft(cluster_id, validated_source)
        run_dir = candidates.cluster_workspace_path(cluster_id) / "runs" / "run-1"
        run_dir.mkdir(parents=True)
        (run_dir / "status.json").write_text(
            json.dumps({
                "run_id": "run-1",
                "cluster_id": cluster_id,
                "status": "finished",
                "source_sha256": hashlib.sha256(validated_source.encode("utf-8")).hexdigest(),
                "modes": {},
            }),
            encoding="utf-8",
        )
        (run_dir / "cpu.log").write_text("CPU evidence\n", encoding="utf-8")
        (run_dir / "gpu0.log").write_text("GPU evidence\n", encoding="utf-8")
        candidates.save_cluster_draft(cluster_id, "print('changed after validation')\n")

        with (
            patch.object(server, "REPO_ROOT", root),
            patch.object(server, "CANDIDATE_STORE", candidates),
            patch.object(server, "DYNAMIC_CONFIRMED_STORE", DynamicConfirmedBugStore(root)),
        ):
            code, payload = server.confirm_candidate_cluster(cluster_id, {})

        assert code == 409
        assert payload["error"] == "saved repro changed after validation; run CPU/GPU validation again"


def test_server_rejects_invalid_candidate_review_metadata():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "demo_runs/api_jobs/job1/Results/torch/crash/torch.add_1.py"
        source.parent.mkdir(parents=True)
        source.write_text('"""INTERNAL ASSERT FAILED"""\nprint(\'candidate\')\n', encoding="utf-8")
        candidates = CandidateStore(root)
        candidates.add(job_id="job1", lib="torch", api="torch.add", category="crash", source_path=source)
        cluster_id = candidates.list_clusters()[0]["cluster_id"]

        with patch.object(server, "CANDIDATE_STORE", candidates):
            code, payload = server.confirm_candidate_cluster(cluster_id, {
                "title": "   ",
                "bug_type": "Internal assertion failure",
                "review_note": "reviewed",
            })

        assert code == 400
        assert payload["error"] == "title cannot be empty"


if __name__ == "__main__":
    test_confirmed_index_excludes_entries_without_repro_source()
    test_dynamic_confirmed_store_archives_evidence_and_requires_id_to_delete()
    test_server_confirms_validated_candidate_and_deletes_dynamic_bug_by_id()
    test_server_rejects_confirmation_when_saved_draft_changed_after_validation()
    test_server_rejects_invalid_candidate_review_metadata()
    print("ok")
