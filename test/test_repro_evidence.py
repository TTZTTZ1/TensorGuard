import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.repro_evidence import classify_execution, execution_profile_for_mode, extract_actual_device, write_report_once  # noqa: E402


def test_negative_sigfpe_returncode_is_reproduced_without_log_text():
    result = classify_execution(returncode=-8, timed_out=False, log_text="")
    assert result["verdict"] == "reproduced"
    assert result["signal"] == "SIGFPE"
    assert result["signal_number"] == 8


def test_unknown_nonzero_exit_needs_review():
    result = classify_execution(returncode=23, timed_out=False, log_text="unclassified")
    assert result["verdict"] == "needs_review"
    assert result["outcome"] == "unknown_nonzero_exit"


def test_timeout_is_not_reported_as_crash():
    result = classify_execution(returncode=None, timed_out=True, log_text="")
    assert result["verdict"] == "timeout"
    assert result["outcome"] == "timeout"


def test_existing_report_is_returned_without_overwrite():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "report.md"
        path.write_text("original", encoding="utf-8")
        assert write_report_once(path, "replacement") == "original"
        assert path.read_text(encoding="utf-8") == "original"


def test_execution_profile_uses_selected_visible_gpu():
    assert execution_profile_for_mode("cpu") == ("cuda_hidden", "")
    assert execution_profile_for_mode("gpu:2") == ("visible_gpu_2", "2")


def test_explicit_device_output_is_recorded_without_guessing():
    assert extract_actual_device("torch: 2.11\ndevice: cuda:0\n") == "cuda:0"
    assert extract_actual_device("CUDA_VISIBLE_DEVICES='0'\nno device line") == "unknown"


if __name__ == "__main__":
    test_negative_sigfpe_returncode_is_reproduced_without_log_text()
    test_unknown_nonzero_exit_needs_review()
    test_timeout_is_not_reported_as_crash()
    test_existing_report_is_returned_without_overwrite()
    test_execution_profile_uses_selected_visible_gpu()
    test_explicit_device_output_is_recorded_without_guessing()
    print("ok")
