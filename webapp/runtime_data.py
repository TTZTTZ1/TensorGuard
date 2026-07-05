"""Runtime inventory and lightweight GPU sampling for the demo server."""

from __future__ import annotations

import importlib.metadata
import platform
import subprocess
import sys
from datetime import datetime
from typing import Callable


RunCommand = Callable[..., subprocess.CompletedProcess]


def collected_at() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _number(value: str, kind):
    value = value.strip()
    if not value or value.upper() in {"N/A", "[N/A]"}:
        return None
    return kind(float(value))


def parse_gpu_inventory(text: str) -> list[dict]:
    gpus = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split(",", 3)]
        if len(parts) != 4:
            continue
        index = _number(parts[0], int)
        memory_total = _number(parts[3], int)
        if index is None:
            continue
        gpus.append(
            {
                "index": index,
                "name": parts[1],
                "driver_version": parts[2],
                "memory_total_mib": memory_total,
            }
        )
    return gpus


def parse_gpu_sample(text: str) -> list[dict]:
    samples = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split(",", 3)]
        if len(parts) != 4:
            continue
        index = _number(parts[0], int)
        if index is None:
            continue
        samples.append(
            {
                "index": index,
                "utilization_percent": _number(parts[1], float),
                "memory_used_mib": _number(parts[2], int),
                "memory_total_mib": _number(parts[3], int),
            }
        )
    return samples


def package_info(distribution: str) -> dict:
    try:
        version = importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return {"installed": False, "version": None}
    except Exception as exc:
        return {"installed": None, "version": None, "error": str(exc)}
    return {"installed": True, "version": version}


def collect_environment(run: RunCommand = subprocess.run) -> dict:
    warnings = []
    gpus = []
    try:
        proc = run(
            [
                "nvidia-smi",
                "--query-gpu=index,name,driver_version,memory.total",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=3,
            check=True,
        )
        gpus = parse_gpu_inventory(proc.stdout)
        if not gpus:
            warnings.append("nvidia-smi returned no GPU inventory")
    except Exception as exc:
        warnings.append(f"GPU inventory unavailable: {exc}")

    return {
        "collected_at": collected_at(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "python": {
            "version": platform.python_version(),
            "executable": sys.executable,
        },
        "frameworks": {
            "torch": package_info("torch"),
            "tensorflow": package_info("tensorflow"),
        },
        "cuda": {
            "available": bool(gpus),
            "driver_version": gpus[0]["driver_version"] if gpus else None,
        },
        "gpus": gpus,
        "warnings": warnings,
    }


def collect_gpu_sample(run: RunCommand = subprocess.run) -> dict:
    warnings = []
    samples = []
    try:
        proc = run(
            [
                "nvidia-smi",
                "--query-gpu=index,utilization.gpu,memory.used,memory.total",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=3,
            check=True,
        )
        samples = parse_gpu_sample(proc.stdout)
        if not samples:
            warnings.append("nvidia-smi returned no GPU samples")
    except Exception as exc:
        warnings.append(f"GPU sample unavailable: {exc}")
    return {
        "collected_at": collected_at(),
        "gpus": samples,
        "warnings": warnings,
    }
