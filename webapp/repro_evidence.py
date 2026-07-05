"""Deterministic reproduction evidence classification and report helpers."""

from __future__ import annotations

import hashlib
import os
import re
import signal
import threading
from pathlib import Path
from typing import Optional


FATAL_SIGNALS = {"SIGABRT", "SIGBUS", "SIGFPE", "SIGILL", "SIGSEGV", "SIGTRAP"}

EVIDENCE_PATTERNS = (
    ("cuda_device_assert", ("device-side assert", "cudaerrorassert"), "reproduced"),
    ("allocator_corruption", ("double free", "free():", "invalid next size", "invalid pointer"), "reproduced"),
    ("internal_assert", ("internal assert failed", "internal assertion failed"), "reproduced"),
    ("fatal_assert", ("check failed", "assertion failure", "fatal error", "fatal:"), "reproduced"),
    ("backend_mismatch", ("varinconsistentcatch", "comparisonfail", "backend mismatch"), "reproduced"),
    ("out_of_memory", ("out of memory", "resource exhausted", "std::bad_alloc"), "needs_review"),
)


def execution_profile_for_mode(mode: str) -> tuple[str, str]:
    if mode == "cpu":
        return "cuda_hidden", ""
    if mode == "gpu0":
        return "visible_gpu_0", "0"
    if mode.startswith("gpu:") and mode[4:].isdigit():
        index = int(mode[4:])
        return f"visible_gpu_{index}", str(index)
    raise ValueError(f"unknown execution mode: {mode}")


def extract_actual_device(log_text: str) -> str:
    """Read only an explicit device declaration emitted by the testcase."""
    pattern = re.compile(
        r"^\s*(?:actual[_ ]device|device)\s*[:=]\s*(cpu|cuda(?::\d+)?|mps|xpu(?::\d+)?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    match = pattern.search(log_text or "")
    return match.group(1).lower() if match else "unknown"


def classify_execution(returncode: Optional[int], timed_out: bool, log_text: str) -> dict:
    """Classify observable process evidence without inferring a root cause."""
    if timed_out:
        return _result("timeout", "timeout", "Execution exceeded the configured timeout.")

    if returncode == 0:
        return _result("not_reproduced", "normal_exit", "Process exited normally with return code 0.")

    if returncode is not None and returncode < 0:
        number = -returncode
        try:
            name = signal.Signals(number).name
        except ValueError:
            name = f"SIGNAL_{number}"
        verdict = "reproduced" if name in FATAL_SIGNALS else "needs_review"
        result = _result(verdict, "signal_exit", f"Process terminated by {name} ({number}).")
        result.update({"signal": name, "signal_number": number})
        return result

    lowered = (log_text or "").lower()
    for outcome, patterns, verdict in EVIDENCE_PATTERNS:
        if any(pattern in lowered for pattern in patterns):
            return _result(verdict, outcome, f"Output matched deterministic evidence category: {outcome}.")

    if returncode is None:
        return _result("needs_review", "launch_error", "No child-process return code was recorded.")

    if "traceback (most recent call last)" in lowered or "error:" in lowered:
        return _result(
            "needs_review",
            "ordinary_exception",
            "Process returned a non-zero code with an exception that requires contextual review.",
        )

    return _result(
        "needs_review",
        "unknown_nonzero_exit",
        f"Process returned unclassified non-zero code {returncode}.",
    )


def _result(verdict: str, outcome: str, reason: str) -> dict:
    return {
        "verdict": verdict,
        "outcome": outcome,
        "reason": reason,
        "signal": None,
        "signal_number": None,
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_report_once(path: Path, content: str) -> str:
    """Create a report atomically; an existing report is always returned unchanged."""
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="replace")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.{threading.get_ident()}.tmp")
    tmp.write_text(content, encoding="utf-8")
    try:
        os.link(tmp, path)
    except FileExistsError:
        pass
    finally:
        tmp.unlink(missing_ok=True)
    return path.read_text(encoding="utf-8", errors="replace")
