import platform
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp import server  # noqa: E402
from webapp.runtime_data import collect_environment  # noqa: E402


def test_overview_api_total_matches_source_lists():
    overview = server.overview_payload()
    torch_count = len(server.load_api_list("torch"))
    tf_count = len(server.load_api_list("tf"))
    assert overview["api_by_lib"] == {"torch": torch_count, "tf": tf_count}
    assert overview["api_total"] == torch_count + tf_count


def test_confirmed_count_only_includes_complete_records():
    bugs = server.load_paper_bugs()
    assert bugs
    assert all("severity" not in bug for bug in bugs)
    for bug in bugs:
        meta_path = ROOT / bug["meta_path"]
        repro_path = meta_path.parent / bug.get("files", {}).get("repro", "repro.py")
        assert meta_path.is_file()
        assert repro_path.is_file()


def test_environment_platform_comes_from_current_runtime():
    environment = collect_environment(run=lambda *args, **kwargs: (_ for _ in ()).throw(FileNotFoundError("nvidia-smi")))
    assert environment["platform"]["system"] == platform.system()
    assert environment["python"]["version"] == platform.python_version()
    assert environment["gpus"] == []
    assert environment["warnings"]


if __name__ == "__main__":
    test_overview_api_total_matches_source_lists()
    test_confirmed_count_only_includes_complete_records()
    test_environment_platform_comes_from_current_runtime()
    print("ok")
