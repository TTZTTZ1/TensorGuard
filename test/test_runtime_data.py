import sys
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.runtime_data import (  # noqa: E402
    collect_environment,
    parse_gpu_inventory,
    parse_gpu_sample,
)
from webapp import server  # noqa: E402


def test_parse_nvidia_smi_inventory():
    text = (
        "0, NVIDIA A800, 550.54.15, 81920\n"
        "1, NVIDIA L40, 550.54.15, 46068\n"
    )
    assert parse_gpu_inventory(text) == [
        {
            "index": 0,
            "name": "NVIDIA A800",
            "driver_version": "550.54.15",
            "memory_total_mib": 81920,
        },
        {
            "index": 1,
            "name": "NVIDIA L40",
            "driver_version": "550.54.15",
            "memory_total_mib": 46068,
        },
    ]


def test_parse_gpu_sample():
    text = "0, 37, 20480, 81920\n"
    assert parse_gpu_sample(text) == [
        {
            "index": 0,
            "utilization_percent": 37.0,
            "memory_used_mib": 20480,
            "memory_total_mib": 81920,
        }
    ]


def test_inventory_failure_returns_warning_not_fake_gpu():
    def fail_run(*args, **kwargs):
        raise FileNotFoundError("nvidia-smi missing")

    data = collect_environment(run=fail_run)
    assert data["cuda"]["available"] is False
    assert data["gpus"] == []
    assert "nvidia-smi missing" in data["warnings"][0]


def test_environment_payload_uses_live_collector():
    expected = {"collected_at": "now", "gpus": [{"name": "Live GPU"}]}
    with patch.object(server, "collect_environment", return_value=expected):
        assert server.environment_payload(force=True) == expected


def test_normalize_terminal_output_keeps_only_latest_carriage_return_frame():
    text = (
        "Loading weights: 0%|0/339\r"
        "Loading weights: 48%|162/339\r"
        "Loading weights: 100%|339/339\n"
        "[qwen_seed] model loaded\n"
    )

    assert server.normalize_terminal_output(text) == (
        "Loading weights: 100%|339/339\n"
        "[qwen_seed] model loaded\n"
    )


def test_normalize_terminal_output_removes_ansi_without_dropping_normal_lines():
    text = "before\n\x1b[32mready\x1b[0m\nafter\n"
    assert server.normalize_terminal_output(text) == "before\nready\nafter\n"


if __name__ == "__main__":
    test_parse_nvidia_smi_inventory()
    test_parse_gpu_sample()
    test_inventory_failure_returns_warning_not_fake_gpu()
    test_environment_payload_uses_live_collector()
    test_normalize_terminal_output_keeps_only_latest_carriage_return_frame()
    test_normalize_terminal_output_removes_ansi_without_dropping_normal_lines()
    print("ok")
