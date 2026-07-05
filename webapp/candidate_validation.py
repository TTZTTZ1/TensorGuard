"""Isolated CPU/GPU execution for human-minimized candidate programs."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from webapp.repro_evidence import classify_execution, execution_profile_for_mode, extract_actual_device
except ModuleNotFoundError:  # Support direct execution through webapp/server.py.
    from repro_evidence import classify_execution, execution_profile_for_mode, extract_actual_device

try:
    import resource
except ImportError:  # pragma: no cover - Windows is not a supported execution host.
    resource = None


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


CORE_LIMIT_RUNNER = (
    "import resource, runpy, sys; "
    "resource.setrlimit(resource.RLIMIT_CORE, (0, 0)); "
    "path = sys.argv[1]; sys.argv = [path]; "
    "runpy.run_path(path, run_name='__main__')"
)


def _tail(path: Path, max_chars: int = 12_000) -> str:
    if not path.is_file():
        return ""
    return path.read_bytes()[-max_chars:].decode("utf-8", errors="replace")


def _write_json(path: Path, payload: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def run_candidate_mode(
    repro: Path,
    mode: str,
    log_path: Path,
    timeout: int,
    *,
    python_executable: str = sys.executable,
) -> dict:
    env = os.environ.copy()
    execution_profile, visible_devices = execution_profile_for_mode(mode)
    env["CUDA_VISIBLE_DEVICES"] = visible_devices
    cmd = (
        [python_executable, "-c", CORE_LIMIT_RUNNER, str(repro)]
        if resource is not None
        else [python_executable, str(repro)]
    )
    started = time.time()
    with log_path.open("w", encoding="utf-8") as log:
        log.write("$ " + " ".join(cmd) + "\n")
        log.write(f"CUDA_VISIBLE_DEVICES={visible_devices!r}\n\n")
        log.flush()
        try:
            process = subprocess.run(
                cmd,
                cwd=repro.parent,
                stdout=log,
                stderr=subprocess.STDOUT,
                env=env,
                text=True,
                timeout=timeout,
                shell=False,
            )
            log_text = _tail(log_path)
            evidence = classify_execution(process.returncode, False, log_text)
            return {
                "status": "finished",
                "returncode": process.returncode,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "execution_profile": execution_profile,
                "actual_device": extract_actual_device(log_text),
                "evidence": evidence,
            }
        except subprocess.TimeoutExpired as exc:
            log.write(f"\n[TIMEOUT] exceeded {timeout}s\n")
            evidence = classify_execution(None, True, "")
            return {
                "status": "timeout",
                "returncode": None,
                "timed_out": True,
                "elapsed_seconds": round(time.time() - started, 3),
                "execution_profile": execution_profile,
                "actual_device": extract_actual_device(_tail(log_path)),
                "evidence": evidence,
                "error": str(exc),
            }
        except Exception as exc:
            log.write(f"\n[SERVER ERROR] {exc}\n")
            evidence = classify_execution(None, False, str(exc))
            return {
                "status": "failed",
                "returncode": None,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "execution_profile": execution_profile,
                "actual_device": "unknown",
                "evidence": evidence,
                "error": str(exc),
            }


def execute_candidate_validation(
    out: Path,
    status: dict,
    *,
    python_executable: str = sys.executable,
) -> dict:
    repro = out / "repro.py"
    timeout = int(status.get("timeout_seconds", 60))
    current = {
        **status,
        "status": "running",
        "started_at": status.get("started_at") or now(),
        "updated_at": now(),
        "modes": {
            mode: {
                "status": "pending",
                "returncode": None,
                "timed_out": False,
                "log": f"{mode}.log",
                "started_at": None,
                "finished_at": None,
            }
            for mode in ("cpu", "gpu0")
        },
    }
    _write_json(out / "status.json", current)
    for mode in ("cpu", "gpu0"):
        current["modes"][mode]["status"] = "running"
        current["modes"][mode]["started_at"] = now()
        current["updated_at"] = now()
        _write_json(out / "status.json", current)
        result = run_candidate_mode(
            repro,
            mode,
            out / f"{mode}.log",
            timeout,
            python_executable=python_executable,
        )
        current["modes"][mode].update(result)
        current["modes"][mode]["finished_at"] = now()
        current["updated_at"] = now()
        _write_json(out / "status.json", current)
    current["status"] = "finished"
    current["updated_at"] = now()
    _write_json(out / "status.json", current)
    return current
