import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.candidates import CandidateStore, recommend_candidate  # noqa: E402
from webapp import server  # noqa: E402


def create_source(root: Path, *, job_id: str = "job1", name: str = "torch.add_1.py", category: str = "crash", body: str | None = None) -> Path:
    source = (
        root
        / "demo_runs"
        / "api_jobs"
        / job_id
        / "Results"
        / "torch"
        / category
        / name
    )
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(body or '"""INTERNAL ASSERT FAILED"""\nimport torch\n', encoding="utf-8")
    return source


def test_candidate_references_exact_job_source_and_deduplicates_hash():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root)
        store = CandidateStore(root)
        first = store.add(
            job_id="job1",
            lib="torch",
            api="torch.add",
            category="crash",
            source_path=source,
        )
        second = store.add(
            job_id="job1",
            lib="torch",
            api="torch.add",
            category="crash",
            source_path=source,
        )
        assert first["id"] == second["id"]
        assert first["source_path"].endswith("torch.add_1.py")
        assert first["status"] == "pending_review"
        assert len(store.list()) == 1


def test_recommendation_excludes_notarget_and_plain_exception():
    assert recommend_candidate("crash", "") is True
    assert recommend_candidate("hangs", "") is True
    assert recommend_candidate("exception", "INTERNAL ASSERT FAILED") is True
    assert recommend_candidate("exception", "ValueError: invalid argument") is False
    assert recommend_candidate("notarget", "") is False


def test_server_creates_candidate_but_cannot_promote_it():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root)
        store = CandidateStore(root)
        payload = {
            "job_id": "job1",
            "lib": "torch",
            "api": "torch.add",
            "category": "crash",
            "source_path": str(source),
        }
        with patch.object(server, "CANDIDATE_STORE", store):
            code, record = server.create_candidate(payload)
            assert code == 201
            code, response = server.update_candidate(record["id"], {"status": "promoted"})
            assert code == 400
            assert "unsupported" in response["error"]


def test_candidate_clusters_filter_generated_noise_and_group_related_errors():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = CandidateStore(root)
        assert_source = create_source(
            root,
            category="exception",
            name="torch.add_1.py",
            body='"""CPU RuntimeError GPU device-side assert triggered"""\nimport torch\n',
        )
        sibling_source = create_source(
            root,
            category="exception",
            name="torch.add_2.py",
            body='"""CUDA error: device-side assert triggered"""\nimport torch\nx=torch.ones(1)\n',
        )
        generated_noise = create_source(
            root,
            category="exception",
            name="torch.add_3.py",
            body='"""SyntaxError: unterminated triple-quoted string literal"""\n',
        )

        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=assert_source)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=sibling_source)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=generated_noise)

        clusters = store.list_clusters()

        assert len(clusters) == 1
        assert clusters[0]["api"] == "torch.add"
        assert clusters[0]["bug_pattern"] == "CPU/GPU exception mismatch / CUDA device-side assert"
        assert clusters[0]["member_count"] == 2
        assert clusters[0]["excluded_count"] == 1
        assert clusters[0]["representative"]["source_path"].endswith("torch.add_1.py")
        assert clusters[0]["cluster_status"] == "needs_minimize"


def test_collect_job_results_registers_trace_and_crash_candidates_idempotently():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = CandidateStore(root)
        valid_source = create_source(
            root,
            category="valid",
            name="torch.add_7.py",
            body="import torch\nresult = torch.add(torch.ones(1), 1)\n",
        )
        create_source(
            root,
            category="crash",
            name="torch.add_8.py",
            body='"""free(): invalid pointer"""\nimport torch\n',
        )
        create_source(
            root,
            category="exception",
            name="torch.add_9.py",
            body='"""ValueError: ordinary invalid argument"""\nimport torch\n',
        )
        create_source(
            root,
            category="exception",
            name="torch.add_10.py",
            body='"""SyntaxError: unterminated triple-quoted string literal"""\n',
        )
        trace = valid_source.parents[1] / "trace.txt"
        trace.write_text(
            "Results/torch 4\n"
            "Testcase 0 torch.add torch.add_7 VarInconsistentCatch 420\n"
            "CPU: tensor([1.])\nGPU: tensor([2.])\n"
            "==== driven race finished ====\n",
            encoding="utf-8",
        )

        first = store.collect_job_results(job_id="job1", lib="torch", api="torch.add")
        second = store.collect_job_results(job_id="job1", lib="torch", api="torch.add")

        assert first["registered"] == 2
        assert first["excluded_noise"] == 1
        assert first["skipped_low_signal"] == 1
        assert len(first["candidate_ids"]) == 2
        assert second["registered"] == 0
        assert second["deduplicated"] == 2
        assert len(store.list()) == 2
        trace_record = next(item for item in store.list() if item["source_path"].endswith("torch.add_7.py"))
        assert "VarInconsistentCatch" in trace_record["error_summary"]


def test_collect_job_results_accepts_high_signal_seed_programs():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = CandidateStore(root)
        seed_source = create_source(
            root,
            category="seed",
            name="torch.add_seed1.py",
            body="import torch\nresult = torch.add(torch.ones(1), 1)\n",
        )
        trace = seed_source.parents[1] / "trace.txt"
        trace.write_text(
            "Results/torch 1\n"
            "Testcase 0 torch.add torch.add_seed1 VarInconsistentCatch 420\n"
            "CPU: tensor([1.])\nGPU: tensor([2.])\n",
            encoding="utf-8",
        )

        report = store.collect_job_results(job_id="job1", lib="torch", api="torch.add")

        assert report["registered"] == 1
        assert report["candidate_ids"] == ["CAND-0001"]
        assert store.list()[0]["category"] == "seed"


def test_server_exposes_candidate_cluster_detail():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(
            root,
            category="exception",
            body='"""INTERNAL ASSERT FAILED at pybind.cpp"""\nimport torch\n',
        )
        store = CandidateStore(root)
        with patch.object(server, "REPO_ROOT", root), patch.object(server, "CANDIDATE_STORE", store):
            store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
            code, listing = server.candidate_clusters_payload()
            assert code == 200
            cluster_id = listing[0]["cluster_id"]
            code, detail = server.candidate_cluster_payload(cluster_id)

        assert code == 200
        assert detail["cluster_id"] == cluster_id
        assert detail["representative_source_code"].startswith('"""INTERNAL ASSERT FAILED')
        assert detail["members"][0]["source_path"].endswith("torch.add_1.py")


def test_server_updates_candidate_cluster_review_status():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        first = create_source(root, category="exception", name="torch.add_1.py")
        second = create_source(root, category="exception", name="torch.add_2.py")
        store = CandidateStore(root)
        with patch.object(server, "CANDIDATE_STORE", store):
            store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=first)
            store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=second)
            code, listing = server.candidate_clusters_payload()
            assert code == 200
            cluster_id = listing[0]["cluster_id"]
            code, updated = server.update_candidate_cluster(cluster_id, {"status": "rejected", "note": "not a framework bug"})

        assert code == 200
        assert updated["cluster_status"] == "rejected"
        assert {member["status"] for member in updated["members"]} == {"rejected"}


def test_candidate_minimization_draft_persists_and_resets_without_touching_source():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        original = '"""INTERNAL ASSERT FAILED"""\nimport torch\nresult = torch.add(torch.ones(1), 1)\n'
        source = create_source(root, category="exception", body=original)
        store = CandidateStore(root)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = store.list_clusters()[0]["cluster_id"]

        initial = store.get_cluster(cluster_id)
        assert initial["minimization_draft"] == original
        assert initial["draft_saved"] is False

        edited = "import torch\nprint(torch.add(torch.ones(1), 1))\n"
        saved = store.save_cluster_draft(cluster_id, edited)
        assert saved["minimization_draft"] == edited
        assert saved["draft_saved"] is True
        assert saved["draft_modified"] is True
        assert source.read_text(encoding="utf-8") == original

        reloaded = CandidateStore(root).get_cluster(cluster_id)
        assert reloaded["minimization_draft"] == edited

        reset = store.reset_cluster_draft(cluster_id)
        assert reset["minimization_draft"] == original
        assert reset["draft_saved"] is True
        assert reset["draft_modified"] is False

        try:
            store.save_cluster_draft("../../outside", "print('unsafe')\n")
        except KeyError:
            pass
        else:
            raise AssertionError("unknown traversal-like cluster id must be rejected")


def test_server_saves_and_resets_candidate_draft():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root, category="exception")
        store = CandidateStore(root)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = store.list_clusters()[0]["cluster_id"]

        with patch.object(server, "CANDIDATE_STORE", store):
            code, saved = server.save_candidate_cluster_draft(cluster_id, {"source": "print('saved')\n"})
            assert code == 200
            assert saved["minimization_draft"] == "print('saved')\n"
            code, reset = server.reset_candidate_cluster_draft(cluster_id)

        assert code == 200
        assert reset["draft_modified"] is False


def test_delete_candidate_cluster_requires_exact_id_and_preserves_result_source():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root, category="exception")
        store = CandidateStore(root)
        store.add(job_id="job1", lib="torch", api="torch.add", category="exception", source_path=source)
        cluster_id = store.list_clusters()[0]["cluster_id"]
        store.save_cluster_draft(cluster_id, "print('draft')\n")
        workspace = store.cluster_workspace_path(cluster_id)

        try:
            store.delete_cluster(cluster_id, confirmation_id="wrong-id")
        except ValueError:
            pass
        else:
            raise AssertionError("wrong confirmation id must not delete candidate cluster")
        assert store.get_cluster(cluster_id) is not None

        store.delete_cluster(cluster_id, confirmation_id=cluster_id)
        assert store.get_cluster(cluster_id) is None
        assert source.is_file()
        assert not workspace.exists()


def test_candidate_ids_do_not_collide_after_cluster_deletion():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = CandidateStore(root)
        apis = ["torch.add", "torch.sub", "torch.mul"]
        for index, api in enumerate(apis, start=1):
            source = create_source(
                root,
                name=f"{api}_{index}.py",
                body=f'"""INTERNAL ASSERT FAILED {api}"""\nimport torch\n',
            )
            store.add(job_id="job1", lib="torch", api=api, category="crash", source_path=source)

        deleted_cluster = next(item for item in store.list_clusters() if item["api"] == "torch.sub")
        store.delete_cluster(deleted_cluster["cluster_id"], confirmation_id=deleted_cluster["cluster_id"])
        replacement = create_source(
            root,
            name="torch.div_4.py",
            body='"""INTERNAL ASSERT FAILED torch.div"""\nimport torch\n',
        )
        added = store.add(job_id="job1", lib="torch", api="torch.div", category="crash", source_path=replacement)

        assert added["id"] == "CAND-0004"
        assert len({record["id"] for record in store.list()}) == 3


if __name__ == "__main__":
    test_candidate_references_exact_job_source_and_deduplicates_hash()
    test_recommendation_excludes_notarget_and_plain_exception()
    test_server_creates_candidate_but_cannot_promote_it()
    test_candidate_clusters_filter_generated_noise_and_group_related_errors()
    test_collect_job_results_registers_trace_and_crash_candidates_idempotently()
    test_collect_job_results_accepts_high_signal_seed_programs()
    test_server_exposes_candidate_cluster_detail()
    test_server_updates_candidate_cluster_review_status()
    test_candidate_minimization_draft_persists_and_resets_without_touching_source()
    test_server_saves_and_resets_candidate_draft()
    test_delete_candidate_cluster_requires_exact_id_and_preserves_result_source()
    test_candidate_ids_do_not_collide_after_cluster_deletion()
    print("ok")
