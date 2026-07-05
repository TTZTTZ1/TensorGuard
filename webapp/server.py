#!/usr/bin/env python3
"""Local presentation server for TensorGuard."""

from __future__ import annotations

import argparse
import codecs
import datetime as dt
import json
import mimetypes
import os
import re
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, unquote, urlparse

try:
    from webapp.runtime_data import collect_environment
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    from runtime_data import collect_environment

try:
    from scripts.demo_metrics import read_metrics
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.demo_metrics import read_metrics

try:
    from webapp.candidates import CandidateStore, recommend_candidate
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    from candidates import CandidateStore, recommend_candidate

try:
    from webapp.candidate_validation import execute_candidate_validation
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    from candidate_validation import execute_candidate_validation

try:
    from webapp.confirmed_bugs import DynamicConfirmedBugStore, load_confirmed_records
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    from confirmed_bugs import DynamicConfirmedBugStore, load_confirmed_records

try:
    from webapp.repro_evidence import classify_execution, execution_profile_for_mode, extract_actual_device, sha256_file, write_report_once
except ModuleNotFoundError:  # Support direct execution as webapp/server.py.
    from repro_evidence import classify_execution, execution_profile_for_mode, extract_actual_device, sha256_file, write_report_once


REPO_ROOT = Path(__file__).resolve().parents[1]
STATIC_ROOT = Path(__file__).resolve().parent / "static"

MANIFEST_PATH = REPO_ROOT / "prompt_library_manifest.json"
PAPER_BUG_ROOT = REPO_ROOT / "reports" / "paper_confirmed_bugs"
PAPER_BUG_INDEX = PAPER_BUG_ROOT / "index.json"
DEMO_ROOT = REPO_ROOT / "demo_runs"
API_JOB_ROOT = DEMO_ROOT / "api_jobs"
REPRO_JOB_ROOT = DEMO_ROOT / "repro_jobs"
CANDIDATE_STORE = CandidateStore(REPO_ROOT)
DYNAMIC_CONFIRMED_STORE = DynamicConfirmedBugStore(REPO_ROOT)

API_LIST_PATHS = {
    "torch": REPO_ROOT / "data" / "torch_apis.txt",
    "tf": REPO_ROOT / "data" / "tf_apis.txt",
}
RESULTS_PATHS = {
    "torch": REPO_ROOT / "Results" / "torch",
    "tf": REPO_ROOT / "Results" / "tf",
}
RESULT_SUBDIRS = ("seed", "valid", "exception", "crash", "notarget", "hangs", "flaky")
TRACE_PATTERNS = (
    "Catch",
    "Fail",
    "INTERNAL ASSERT",
    "device-side assert",
    "invalid argument",
    "Segmentation fault",
    "Floating point exception",
    "free()",
    "Aborted",
    "Check failed",
)
API_STAGE_ORDER = ("prompt_check", "qwen_seed", "ev_generation", "driver", "summary")
API_JOB_LOG_NAMES = frozenset(("01_qwen_seed.log", "02_ev_generation.log", "03_driver.log"))
LOG_CHUNK_BYTES = 256 * 1024
REPRO_TIMEOUT_SECONDS = 60
ENVIRONMENT_CACHE_SECONDS = 30
_ENVIRONMENT_CACHE: Dict[str, Any] = {"expires_at": 0.0, "data": None}
_ENVIRONMENT_LOCK = threading.Lock()


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def environment_payload(force: bool = False) -> dict:
    current = time.monotonic()
    with _ENVIRONMENT_LOCK:
        cached = _ENVIRONMENT_CACHE.get("data")
        if not force and cached is not None and current < _ENVIRONMENT_CACHE["expires_at"]:
            return cached
        data = collect_environment()
        _ENVIRONMENT_CACHE["data"] = data
        _ENVIRONMENT_CACHE["expires_at"] = current + ENVIRONMENT_CACHE_SECONDS
        return data


def safe_name(value: str) -> str:
    keep = []
    for ch in value:
        keep.append(ch if ch.isalnum() or ch in "._-" else "_")
    name = "".join(keep).strip("._")
    return name or "item"


def unique_job_directory(root: Path, base_id: str) -> tuple[str, Path]:
    root.mkdir(parents=True, exist_ok=True)
    suffix = 1
    while True:
        job_id = base_id if suffix == 1 else f"{base_id}_{suffix}"
        out = root / job_id
        try:
            out.mkdir()
            return job_id, out
        except FileExistsError:
            suffix += 1


def display_bug_id(bug_id: str) -> str:
    return bug_id.removeprefix("PAPER-")


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_json(path: Path, default: Any) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def write_response(handler: BaseHTTPRequestHandler, status: int, body: bytes, content_type: str) -> None:
    handler.send_response(status)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def send_json(handler: BaseHTTPRequestHandler, payload: Any, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    write_response(handler, status, body, "application/json; charset=utf-8")


def send_text(handler: BaseHTTPRequestHandler, text: str, status: int = 200, content_type: str = "text/plain") -> None:
    write_response(handler, status, text.encode("utf-8"), f"{content_type}; charset=utf-8")


def load_manifest() -> dict:
    return read_json(MANIFEST_PATH, {"libraries": {"torch": {}, "tf": {}}, "total_apis": 0})


def load_api_list(lib: str) -> list[str]:
    path = API_LIST_PATHS.get(lib)
    if path is None or not path.is_file():
        return []
    apis = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            api = line.strip()
            if api and not api.startswith("#"):
                apis.append(api)
    return apis


def manifest_entry(lib: str, api: str) -> Optional[dict]:
    return load_manifest().get("libraries", {}).get(lib, {}).get(api)


def prompt_path(lib: str, api: str) -> Path:
    return REPO_ROOT / "experiment" / lib / api / "prompts" / "structured_info.txt"


def count_py(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for child in path.iterdir() if child.is_file() and child.suffix == ".py")


def result_counts(results_dir: Path) -> dict:
    return {name: count_py(results_dir / name) for name in RESULT_SUBDIRS}


def empty_result_counts() -> dict:
    return {name: 0 for name in RESULT_SUBDIRS}


def result_counts_by_api(lib: str) -> dict[str, dict]:
    root = RESULTS_PATHS[lib]
    counts_by_api: dict[str, dict] = {}
    for name in RESULT_SUBDIRS:
        folder = root / name
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if not path.is_file() or path.suffix != ".py":
                continue
            api_name = path.stem.rsplit("_", 1)[0]
            counts_by_api.setdefault(api_name, empty_result_counts())[name] += 1
    return counts_by_api


def api_result_counts(lib: str, api: str) -> dict:
    return result_counts_by_api(lib).get(api, empty_result_counts())


def results_api_set(lib: str) -> set[str]:
    root = RESULTS_PATHS[lib]
    known = set(load_api_list(lib))
    found = set()
    for subdir in RESULT_SUBDIRS:
        folder = root / subdir
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if not path.is_file() or path.suffix != ".py":
                continue
            api_name = path.stem.rsplit("_", 1)[0]
            if api_name in known:
                found.add(api_name)
    return found


def trace_path(lib: str) -> Path:
    return RESULTS_PATHS[lib] / "trace.txt"


def trace_hit_count(path: Path) -> int:
    if not path.is_file():
        return 0
    total = 0
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if any(pattern in line for pattern in TRACE_PATTERNS):
                total += 1
    return total


ANSI_ESCAPE_RE = re.compile(r"\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def normalize_terminal_output(text: str) -> str:
    """Render captured terminal control sequences as readable plain text."""
    text = ANSI_ESCAPE_RE.sub("", text).replace("\r\n", "\n")
    rendered: list[str] = []
    current: list[str] = []
    for char in text:
        if char == "\r":
            current.clear()
        elif char == "\n":
            rendered.append("".join(current) + "\n")
            current.clear()
        elif char == "\b":
            if current:
                current.pop()
        else:
            current.append(char)
    if current:
        rendered.append("".join(current))
    return "".join(rendered)


def tail(path: Path, max_chars: int = 8000) -> str:
    if not path.is_file():
        return ""
    data = path.read_bytes()
    return normalize_terminal_output(data[-max_chars:].decode("utf-8", errors="replace"))


def latest_summaries(root: Path, limit: int = 6) -> list[dict]:
    if not root.is_dir():
        return []
    paths = sorted(root.glob("**/summary.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out = []
    for path in paths[:limit]:
        item = read_json(path, {})
        if item:
            item["_path"] = rel(path)
            out.append(item)
    return out


def latest_api_job(lib: str, api: str) -> Optional[dict]:
    if not API_JOB_ROOT.is_dir():
        return None
    candidates = []
    for status_path in API_JOB_ROOT.glob("*/status.json"):
        status = read_json(status_path, {})
        if status.get("lib") == lib and status.get("api") == api:
            candidates.append((status_path.stat().st_mtime, status_path.parent, status))
    if not candidates:
        return None
    _, job_dir, status = sorted(candidates, key=lambda item: item[0], reverse=True)[0]
    summary = read_json(job_dir / "summary.json", {})
    return {
        "job_id": status.get("job_id") or job_dir.name,
        "out": rel(job_dir),
        "status": status.get("status", "pending"),
        "stage": status.get("stage", "init"),
        "updated_at": status.get("updated_at"),
        "summary_status": summary.get("status"),
        "mutation_model": status.get("mutation_model") or summary.get("mutation_model"),
        "error": status.get("error") or summary.get("error"),
    }


def overview_payload() -> dict:
    manifest = load_manifest()
    manifest_libs = manifest.get("libraries", {})
    api_lists = {lib: load_api_list(lib) for lib in ("torch", "tf")}
    api_counts = {lib: len(apis) for lib, apis in api_lists.items()}
    prompt_ready = {
        lib: sum(1 for api in apis if api in manifest_libs.get(lib, {}) or prompt_path(lib, api).is_file())
        for lib, apis in api_lists.items()
    }
    results = {}
    for lib in ("torch", "tf"):
        root = RESULTS_PATHS[lib]
        trace = trace_path(lib)
        results[lib] = {
            "path": rel(root),
            "exists": root.is_dir(),
            "api_count": len(results_api_set(lib)) if root.is_dir() else 0,
            "counts": result_counts(root),
            "trace_path": rel(trace),
            "trace_exists": trace.is_file(),
            "trace_hits": trace_hit_count(trace),
        }

    paper_bugs = load_paper_bugs()
    bug_by_framework: Dict[str, int] = {}
    for bug in paper_bugs:
        fw = bug.get("framework", "Unknown")
        bug_by_framework[fw] = bug_by_framework.get(fw, 0) + 1

    return {
        "api_total": sum(api_counts.values()),
        "api_by_lib": api_counts,
        "prompt_ready_total": sum(prompt_ready.values()),
        "prompt_ready_by_lib": prompt_ready,
        "results": results,
        "paper_bug_total": len(paper_bugs),
        "paper_bug_by_framework": bug_by_framework,
        "latest_api_jobs": latest_summaries(API_JOB_ROOT),
        "latest_repro_jobs": latest_repro_summaries(),
        "sources": {
            "torch_api_list": rel(API_LIST_PATHS["torch"]),
            "tf_api_list": rel(API_LIST_PATHS["tf"]),
            "prompt_library": "experiment/<lib>/<api>/prompts/",
            "api_jobs": rel(API_JOB_ROOT),
            "repro_jobs": rel(REPRO_JOB_ROOT),
        },
    }


def api_list_payload(lib: str, query: str = "", limit: int = 200) -> list[dict]:
    query_l = query.lower().strip()
    manifest_lib = load_manifest().get("libraries", {}).get(lib, {})
    counts_by_api = result_counts_by_api(lib)
    apis = load_api_list(lib)
    if query_l:
        apis = [api for api in apis if query_l in api.lower()]
    out = []
    for api in apis[:limit]:
        entry = manifest_lib.get(api, {})
        ppath = prompt_path(lib, api)
        counts = counts_by_api.get(api, empty_result_counts())
        out.append(
            {
                "api": api,
                "lib": lib,
                "has_prompt": api in manifest_lib or ppath.is_file(),
                "prompt_path": rel(ppath),
                "result_counts": counts,
                "has_results": any(counts.values()),
                "manifest_entry": entry,
            }
        )
    return out


def api_detail_payload(lib: str, api: str) -> tuple[int, dict]:
    if lib not in ("torch", "tf"):
        return 400, {"error": "lib must be torch or tf"}
    if api not in load_api_list(lib):
        return 404, {"error": f"api not found in data/{lib}_apis.txt"}
    entry = manifest_entry(lib, api) or {}
    ppath = prompt_path(lib, api)
    counts = api_result_counts(lib, api)
    return 200, {
        "api": api,
        "lib": lib,
        "api_list": rel(API_LIST_PATHS[lib]),
        "has_prompt": bool(entry) or ppath.is_file(),
        "prompt_path": rel(ppath),
        "prompt_exists": ppath.is_file(),
        "results_path": rel(RESULTS_PATHS[lib]),
        "result_counts": counts,
        "has_results": any(counts.values()),
        "manifest_entry": entry,
        "latest_job": latest_api_job(lib, api),
    }


def initial_api_status(
    job_id: str,
    lib: str,
    api: str,
    mode: str,
    qwen_model: str,
    mutation_model: str,
    cuda_device: str,
) -> dict:
    return {
        "job_id": job_id,
        "lib": lib,
        "api": api,
        "mode": mode,
        "qwen_model": qwen_model,
        "mutation_model": mutation_model,
        "cuda_device": cuda_device,
        "status": "pending",
        "stage": "launch",
        "stages": {stage: "pending" for stage in API_STAGE_ORDER},
        "error": None,
        "updated_at": now(),
    }


def start_api_job(payload: dict) -> tuple[int, dict]:
    lib = payload.get("lib", "torch")
    api = payload.get("api", "")
    mode = payload.get("mode", "demo")
    qwen_model = payload.get("qwen_model", "../Qwen2.5-Coder-7B-Instruct")
    mut_model = payload.get("mut_model", "facebook/incoder-1B")
    cuda_device = str(payload.get("cuda_device", "0"))

    if lib not in ("torch", "tf"):
        return 400, {"error": "lib must be torch or tf"}
    if mode not in ("demo", "normal"):
        return 400, {"error": "mode must be demo or normal"}
    if api not in load_api_list(lib):
        return 400, {"error": f"api not found in {rel(API_LIST_PATHS[lib])}"}
    if not prompt_path(lib, api).is_file() and manifest_entry(lib, api) is None:
        return 400, {"error": f"prompt library missing for {lib}:{api}"}

    ts = time.strftime("%Y%m%d_%H%M%S")
    job_id, out = unique_job_directory(API_JOB_ROOT, f"api_{safe_name(lib)}_{safe_name(api)}_{ts}")
    server_log = out / "server_launch.log"
    launch_status = initial_api_status(job_id, lib, api, mode, qwen_model, mut_model, cuda_device)
    write_json(out / "status.json", launch_status)
    cmd = [
        sys.executable,
        "scripts/run_one_api_demo.py",
        "--lib",
        lib,
        "--api",
        api,
        "--constraints_dir",
        f"experiment/{lib}",
        "--qwen_model",
        qwen_model,
        "--mut_model",
        mut_model,
        "--out",
        rel(out),
        "--mode",
        mode,
        "--job_id",
        job_id,
        "--cuda_device",
        cuda_device,
    ]

    def _launch() -> None:
        with server_log.open("w", encoding="utf-8") as log:
            log.write("$ " + " ".join(cmd) + "\n\n")
            log.flush()
            try:
                subprocess.Popen(
                    cmd,
                    cwd=REPO_ROOT,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    text=True,
                )
            except Exception as exc:
                failed = read_json(out / "status.json", launch_status)
                failed["status"] = "failed"
                failed["error"] = f"failed to launch pipeline: {exc}"
                failed["updated_at"] = now()
                write_json(out / "status.json", failed)
                log.write(f"\n[SERVER ERROR] {exc}\n")

    threading.Thread(target=_launch, daemon=True).start()
    return 202, {"job_id": job_id, "out": rel(out)}


def find_api_job(job_id: str) -> Optional[Path]:
    direct = API_JOB_ROOT / job_id
    if direct.is_dir():
        return direct
    if not API_JOB_ROOT.is_dir():
        return None
    for status_path in API_JOB_ROOT.glob("**/status.json"):
        status = read_json(status_path, {})
        if status.get("job_id") == job_id:
            return status_path.parent
    return None


def api_job_log_chunk(job_id: str, log_name: str, offset: int) -> tuple[int, dict]:
    if log_name not in API_JOB_LOG_NAMES:
        return 400, {"error": "unsupported API job log"}
    if not isinstance(offset, int) or offset < 0:
        return 400, {"error": "offset must be a non-negative integer"}
    out = find_api_job(job_id)
    if out is None:
        return 404, {"error": "api job not found"}

    path = out / "logs" / log_name
    if not path.is_file():
        return 200, {
            "job_id": job_id,
            "log_name": log_name,
            "text": "",
            "offset": 0,
            "next_offset": 0,
            "size_bytes": 0,
            "has_more": False,
            "reset": offset > 0,
        }

    size = path.stat().st_size
    reset = offset > size
    start = 0 if reset else offset
    with path.open("rb") as stream:
        stream.seek(start)
        data = stream.read(LOG_CHUNK_BYTES)
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    text = decoder.decode(data, final=start + len(data) >= size)
    buffered, _ = decoder.getstate()
    consumed = len(data) - len(buffered)
    next_offset = start + consumed
    return 200, {
        "job_id": job_id,
        "log_name": log_name,
        "text": normalize_terminal_output(text),
        "offset": start,
        "next_offset": next_offset,
        "size_bytes": size,
        "has_more": next_offset < size,
        "reset": reset,
    }


def list_job_result_files(out: Path, lib: str, api: str) -> dict[str, list[dict]]:
    root = out / "Results" / lib
    files: dict[str, list[dict]] = {category: [] for category in RESULT_SUBDIRS}
    for category in RESULT_SUBDIRS:
        folder = root / category
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.py")):
            if path.stem.rsplit("_", 1)[0] != api:
                continue
            source = path.read_text(encoding="utf-8", errors="replace")
            files[category].append(
                {
                    "name": path.name,
                    "path": rel(path),
                    "size_bytes": path.stat().st_size,
                    "source_excerpt": source[:4000],
                    "recommended": recommend_candidate(category, source[:4000]),
                }
            )
    return files


def api_job_payload(job_id: str) -> tuple[int, dict]:
    out = find_api_job(job_id)
    if out is None:
        return 404, {"error": "api job not found"}
    status = read_json(out / "status.json", {})
    summary = read_json(out / "summary.json", {})
    logs = {}
    if (out / "logs").is_dir():
        for path in sorted((out / "logs").glob("*.log")):
            logs[path.name] = tail(path)
    logs["server_launch.log"] = tail(out / "server_launch.log")
    return 200, {
        "job_id": job_id,
        "out": rel(out),
        "status": status,
        "summary": summary,
        "metrics": read_metrics(out / "metrics.jsonl", limit=2000),
        "environment": read_json(out / "environment.json", {}),
        "result_files": list_job_result_files(
            out,
            str(status.get("lib") or summary.get("lib") or ""),
            str(status.get("api") or summary.get("api") or ""),
        ),
        "logs": logs,
    }


def candidate_payload(candidate_id: str) -> tuple[int, dict]:
    record = CANDIDATE_STORE.get(candidate_id)
    if record is None:
        return 404, {"error": "candidate not found"}
    source = REPO_ROOT / record.get("source_path", "")
    payload = dict(record)
    payload["source_exists"] = source.is_file()
    payload["source_code"] = source.read_text(encoding="utf-8", errors="replace") if source.is_file() else ""
    return 200, payload


def candidate_clusters_payload() -> tuple[int, list[dict]]:
    return 200, CANDIDATE_STORE.list_clusters()


def candidate_cluster_payload(cluster_id: str) -> tuple[int, dict]:
    cluster = CANDIDATE_STORE.get_cluster(cluster_id)
    if cluster is None:
        return 404, {"error": "candidate cluster not found"}
    latest = latest_candidate_validation(cluster_id)
    cluster["latest_validation_job_id"] = latest.get("run_id") if latest else None
    cluster["latest_validation"] = latest
    return 200, cluster


def create_candidate(payload: dict) -> tuple[int, dict]:
    required = ("job_id", "lib", "api", "category", "source_path")
    missing = [name for name in required if not payload.get(name)]
    if missing:
        return 400, {"error": f"missing candidate fields: {', '.join(missing)}"}
    source = Path(str(payload["source_path"]))
    if not source.is_absolute():
        source = REPO_ROOT / source
    try:
        record = CANDIDATE_STORE.add(
            job_id=str(payload["job_id"]),
            lib=str(payload["lib"]),
            api=str(payload["api"]),
            category=str(payload["category"]),
            source_path=source,
            note=str(payload.get("note", "")),
        )
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return 201, record


def update_candidate(candidate_id: str, payload: dict) -> tuple[int, dict]:
    status = str(payload.get("status", ""))
    if status not in {"pending_review", "reproduced", "needs_review", "rejected"}:
        return 400, {"error": "unsupported web candidate status"}
    try:
        record = CANDIDATE_STORE.update_status(candidate_id, status, payload.get("note"))
    except KeyError:
        return 404, {"error": "candidate not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return 200, record


def update_candidate_cluster(cluster_id: str, payload: dict) -> tuple[int, dict]:
    status = str(payload.get("status", ""))
    if status not in {"pending_review", "reproduced", "needs_review", "rejected"}:
        return 400, {"error": "unsupported web candidate status"}
    try:
        cluster = CANDIDATE_STORE.update_cluster_status(cluster_id, status, payload.get("note"))
    except KeyError:
        return 404, {"error": "candidate cluster not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return 200, cluster


def save_candidate_cluster_draft(cluster_id: str, payload: dict) -> tuple[int, dict]:
    try:
        CANDIDATE_STORE.save_cluster_draft(cluster_id, payload.get("source"))
    except KeyError:
        return 404, {"error": "candidate cluster not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return candidate_cluster_payload(cluster_id)


def reset_candidate_cluster_draft(cluster_id: str) -> tuple[int, dict]:
    try:
        CANDIDATE_STORE.reset_cluster_draft(cluster_id)
    except KeyError:
        return 404, {"error": "candidate cluster not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return candidate_cluster_payload(cluster_id)


def delete_candidate_cluster(cluster_id: str, payload: dict) -> tuple[int, dict]:
    try:
        CANDIDATE_STORE.delete_cluster(cluster_id, confirmation_id=str(payload.get("confirmation_id", "")))
    except KeyError:
        return 404, {"error": "candidate cluster not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return 200, {"deleted": cluster_id}


def _candidate_review_metadata(cluster: dict, payload: dict) -> tuple[dict | None, str | None]:
    defaults = cluster.get("review_defaults") if isinstance(cluster.get("review_defaults"), dict) else {}
    limits = {"title": 200, "bug_type": 160, "review_note": 4000}
    result = {}
    for field, limit in limits.items():
        raw = payload.get(field, defaults.get(field, ""))
        if not isinstance(raw, str):
            return None, f"{field} must be text"
        value = raw.strip()
        if not value:
            return None, f"{field} cannot be empty"
        if len(value) > limit:
            return None, f"{field} exceeds {limit} characters"
        result[field] = value
    return result, None


def confirm_candidate_cluster(cluster_id: str, payload: dict) -> tuple[int, dict]:
    cluster = CANDIDATE_STORE.get_cluster(cluster_id)
    if cluster is None:
        return 404, {"error": "candidate cluster not found"}
    review_metadata, review_error = _candidate_review_metadata(cluster, payload)
    if review_error is not None:
        return 400, {"error": review_error}
    if not cluster.get("draft_saved"):
        return 409, {"error": "save repro.py before confirming the Bug"}
    validation = latest_candidate_validation(cluster_id)
    if not validation or validation.get("status") != "finished":
        return 409, {"error": "finish CPU/GPU validation before confirming the Bug"}
    draft_path = CANDIDATE_STORE.cluster_draft_path(cluster_id)
    if validation.get("source_sha256") != sha256_file(draft_path):
        return 409, {"error": "saved repro changed after validation; run CPU/GPU validation again"}
    validation_dir = find_candidate_validation_job(str(validation.get("run_id", "")))
    if validation_dir is None:
        return 409, {"error": "candidate validation evidence is unavailable"}
    try:
        record = DYNAMIC_CONFIRMED_STORE.archive_candidate(
            cluster=cluster,
            repro_path=draft_path,
            validation_dir=validation_dir,
            environment=environment_payload(force=True),
            review_metadata=review_metadata,
        )
        CANDIDATE_STORE.update_cluster_status(cluster_id, "promoted", f"confirmed as {record['id']}")
    except ValueError as exc:
        return 409, {"error": str(exc)}
    status, detail = paper_bug_detail(str(record["id"]))
    return (201 if status == 200 else status), detail


def delete_confirmed_bug(bug_id: str, payload: dict) -> tuple[int, dict]:
    record = next((item for item in load_paper_bugs() if item.get("id") == bug_id), None)
    if record is None:
        return 404, {"error": "confirmed Bug not found"}
    if not record.get("dynamic"):
        return 403, {"error": "curated baseline Bugs are read-only"}
    try:
        DYNAMIC_CONFIRMED_STORE.delete(bug_id, confirmation_id=str(payload.get("confirmation_id", "")))
    except KeyError:
        return 404, {"error": "confirmed Bug not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}
    return 200, {"deleted": bug_id}


def candidate_validation_root(cluster_id: str) -> Path:
    return CANDIDATE_STORE.cluster_workspace_path(cluster_id) / "runs"


def latest_candidate_validation(cluster_id: str) -> Optional[dict]:
    try:
        root = candidate_validation_root(cluster_id)
    except KeyError:
        return None
    status_paths = sorted(
        root.glob("*/status.json") if root.is_dir() else [],
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not status_paths:
        return None
    status_path = status_paths[0]
    payload = read_json(status_path, {})
    payload["logs"] = {
        mode: tail(status_path.parent / f"{mode}.log", max_chars=12_000)
        for mode in ("cpu", "gpu0")
    }
    return payload


def start_candidate_validation(cluster_id: str, payload: dict) -> tuple[int, dict]:
    try:
        if "source" in payload:
            CANDIDATE_STORE.save_cluster_draft(cluster_id, payload.get("source"))
        draft = CANDIDATE_STORE.cluster_draft_path(cluster_id)
        runs_root = candidate_validation_root(cluster_id)
    except KeyError:
        return 404, {"error": "candidate cluster not found"}
    except ValueError as exc:
        return 400, {"error": str(exc)}

    try:
        timeout = max(1, min(int(payload.get("timeout", 60) or 60), 300))
    except (TypeError, ValueError):
        return 400, {"error": "timeout must be an integer between 1 and 300"}
    ts = time.strftime("%Y%m%d_%H%M%S")
    run_id, out = unique_job_directory(runs_root, f"candidate_{safe_name(cluster_id)}_{ts}")
    (out / "repro.py").write_text(draft.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
    status = {
        "run_id": run_id,
        "cluster_id": cluster_id,
        "status": "pending",
        "source_sha256": sha256_file(out / "repro.py"),
        "timeout_seconds": timeout,
        "started_at": now(),
        "updated_at": now(),
        "modes": {},
    }
    write_json(out / "status.json", status)

    def _worker() -> None:
        try:
            execute_candidate_validation(out, status)
        except Exception as exc:
            failed = read_json(out / "status.json", status)
            failed["status"] = "failed"
            failed["error"] = str(exc)
            failed["updated_at"] = now()
            write_json(out / "status.json", failed)

    threading.Thread(target=_worker, daemon=True).start()
    return 202, {
        "run_id": run_id,
        "cluster_id": cluster_id,
        "source_sha256": status["source_sha256"],
    }


def find_candidate_validation_job(run_id: str) -> Optional[Path]:
    root = CANDIDATE_STORE.index_path.parent / "workspaces"
    if not root.is_dir():
        return None
    for status_path in root.glob("*/runs/*/status.json"):
        if read_json(status_path, {}).get("run_id") == run_id:
            return status_path.parent
    return None


def candidate_validation_job_payload(run_id: str) -> tuple[int, dict]:
    out = find_candidate_validation_job(run_id)
    if out is None:
        return 404, {"error": "candidate validation job not found"}
    status = read_json(out / "status.json", {})
    status["logs"] = {
        mode: tail(out / f"{mode}.log", max_chars=12_000)
        for mode in ("cpu", "gpu0")
    }
    return 200, status


def load_paper_bugs() -> list[dict]:
    items = [
        *load_confirmed_records(PAPER_BUG_INDEX, REPO_ROOT),
        *DYNAMIC_CONFIRMED_STORE.list(),
    ]
    out = []
    for item in items:
        item = dict(item)
        item["meta_path"] = item.get("path", "")
        item["display_id"] = display_bug_id(str(item.get("id", "")))
        item["deletable"] = bool(item.get("dynamic"))
        out.append(item)
    return out


def paper_bug_detail(bug_id: str) -> tuple[int, dict]:
    for item in load_paper_bugs():
        if item.get("id") != bug_id:
            continue
        meta_path = REPO_ROOT / item.get("path", "")
        if not meta_path.is_file():
            return 404, {"error": "bug meta not found"}
        meta = read_json(meta_path, {})
        meta.pop("severity", None)
        bug_dir = meta_path.parent
        repro = bug_dir / meta.get("files", {}).get("repro", "repro.py")
        report = bug_dir / meta.get("files", {}).get("report", "report.md")
        latest_repro = latest_repro_summary_for_bug(bug_id)
        return 200, {
            "index": item,
            "meta": meta,
            "display_id": display_bug_id(bug_id),
            "bug_dir": rel(bug_dir),
            "repro_path": rel(repro),
            "report_path": rel(report),
            "repro_code": repro.read_text(encoding="utf-8", errors="replace") if repro.is_file() else "",
            "report_markdown": report.read_text(encoding="utf-8", errors="replace") if report.is_file() else "",
            "latest_repro_job_id": latest_repro.get("job_id") if latest_repro else None,
        }
    return 404, {"error": "confirmed bug not found"}


def read_body(handler: BaseHTTPRequestHandler) -> tuple[bool, dict]:
    length = int(handler.headers.get("Content-Length", "0"))
    raw = handler.rfile.read(length)
    try:
        payload = json.loads(raw.decode("utf-8")) if raw else {}
        if not isinstance(payload, dict):
            return False, {"error": "JSON body must be an object"}
        return True, payload
    except Exception:
        return False, {"error": "invalid JSON"}


def repro_status_template(job_id: str, bug_id: str, modes: list[str], out: Path) -> dict:
    return {
        "job_id": job_id,
        "bug_id": bug_id,
        "status": "pending",
        "started_at": now(),
        "updated_at": now(),
        "out": rel(out),
        "timeout_seconds": REPRO_TIMEOUT_SECONDS,
        "modes": {
            mode: {
                "status": "pending",
                "returncode": None,
                "timed_out": False,
                "log": rel(out / f"{mode}.log"),
                "started_at": None,
                "finished_at": None,
                "execution_profile": execution_profile_for_mode(mode)[0],
                "actual_device": "unknown",
                "evidence": None,
            }
            for mode in modes
        },
        "report": rel(out / "report.md"),
        "error": None,
    }


def run_repro_mode(repro: Path, mode: str, log_path: Path, timeout: int) -> dict:
    env = os.environ.copy()
    execution_profile, visible_devices = execution_profile_for_mode(mode)
    env["CUDA_VISIBLE_DEVICES"] = visible_devices

    cmd = [sys.executable, str(repro)]
    started = time.time()
    with log_path.open("w", encoding="utf-8") as log:
        log.write("$ " + " ".join(cmd) + "\n")
        log.write(f"CUDA_VISIBLE_DEVICES={env.get('CUDA_VISIBLE_DEVICES', '')!r}\n\n")
        log.flush()
        try:
            proc = subprocess.run(
                cmd,
                cwd=repro.parent,
                stdout=log,
                stderr=subprocess.STDOUT,
                env=env,
                text=True,
                timeout=timeout,
            )
            log_text = tail(log_path)
            evidence = classify_execution(proc.returncode, False, log_text)
            return {
                "status": "finished",
                "returncode": proc.returncode,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "execution_profile": execution_profile,
                "actual_device": extract_actual_device(log_text),
                "evidence": evidence,
                "verdict": evidence["verdict"],
            }
        except subprocess.TimeoutExpired as exc:
            log.write(f"\n[TIMEOUT] exceeded {timeout}s\n")
            evidence = classify_execution(None, True, "")
            return {
                "status": "timeout",
                "returncode": None,
                "timed_out": True,
                "elapsed_seconds": round(time.time() - started, 3),
                "error": str(exc),
                "execution_profile": execution_profile,
                "actual_device": extract_actual_device(tail(log_path)),
                "evidence": evidence,
                "verdict": evidence["verdict"],
            }
        except Exception as exc:
            log.write(f"\n[SERVER ERROR] {exc}\n")
            evidence = classify_execution(None, False, str(exc))
            return {
                "status": "failed",
                "returncode": None,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "error": str(exc),
                "execution_profile": execution_profile,
                "actual_device": "unknown",
                "evidence": evidence,
                "verdict": evidence["verdict"],
            }


def start_repro_job(bug_id: str, payload: dict) -> tuple[int, dict]:
    status_code, detail = paper_bug_detail(bug_id)
    if status_code != 200:
        return status_code, detail
    meta = detail["meta"]
    repro = REPO_ROOT / detail["repro_path"]
    if not repro.is_file():
        return 404, {"error": "repro.py not found"}

    requested = payload.get("modes", ["cpu"])
    if isinstance(requested, str):
        requested = [requested]
    inventory = environment_payload(force=True)
    gpu_modes = {f"gpu:{gpu['index']}" for gpu in inventory.get("gpus", [])}
    allowed_modes = {"cpu", *gpu_modes}
    modes = list(dict.fromkeys(mode for mode in requested if mode in allowed_modes))
    if not modes:
        return 400, {"error": "modes must include cpu or a GPU reported by /api/environment"}

    timeout = int(payload.get("timeout", REPRO_TIMEOUT_SECONDS) or REPRO_TIMEOUT_SECONDS)
    ts = time.strftime("%Y%m%d_%H%M%S")
    job_id, out = unique_job_directory(REPRO_JOB_ROOT, f"repro_{safe_name(display_bug_id(bug_id))}_{ts}")
    status = repro_status_template(job_id, bug_id, modes, out)
    status["timeout_seconds"] = timeout
    status["meta"] = {
        "title": meta.get("title", ""),
        "framework": meta.get("framework", ""),
        "api": meta.get("api", ""),
        "bug_type": meta.get("bug_type", ""),
    }
    write_json(out / "environment.json", inventory)
    status["environment"] = rel(out / "environment.json")
    write_json(out / "status.json", status)
    (out / "repro.py").write_text(repro.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")

    def _worker() -> None:
        current = read_json(out / "status.json", status)
        current["status"] = "running"
        current["updated_at"] = now()
        write_json(out / "status.json", current)
        for mode in modes:
            current = read_json(out / "status.json", current)
            current["modes"][mode]["status"] = "running"
            current["modes"][mode]["started_at"] = now()
            current["updated_at"] = now()
            write_json(out / "status.json", current)
            result = run_repro_mode(repro, mode, out / f"{mode}.log", timeout)
            current = read_json(out / "status.json", current)
            current["modes"][mode].update(result)
            current["modes"][mode]["finished_at"] = now()
            current["updated_at"] = now()
            write_json(out / "status.json", current)
        current = read_json(out / "status.json", current)
        current["status"] = "finished"
        current["updated_at"] = now()
        write_json(out / "status.json", current)

    threading.Thread(target=_worker, daemon=True).start()
    return 202, {"job_id": job_id, "out": rel(out)}


def find_repro_job(job_id: str) -> Optional[Path]:
    direct = REPRO_JOB_ROOT / job_id
    if direct.is_dir():
        return direct
    if not REPRO_JOB_ROOT.is_dir():
        return None
    for status_path in REPRO_JOB_ROOT.glob("**/status.json"):
        status = read_json(status_path, {})
        if status.get("job_id") == job_id:
            return status_path.parent
    return None


def repro_job_payload(job_id: str) -> tuple[int, dict]:
    out = find_repro_job(job_id)
    if out is None:
        return 404, {"error": "repro job not found"}
    status = read_json(out / "status.json", {})
    for mode, item in status.get("modes", {}).items():
        if item.get("evidence") or item.get("status") not in ("finished", "timeout", "failed"):
            continue
        evidence = classify_execution(
            item.get("returncode"),
            bool(item.get("timed_out")),
            tail(out / f"{mode}.log"),
        )
        item["evidence"] = evidence
        item["verdict"] = evidence["verdict"]
    logs = {}
    for mode in status.get("modes", {}):
        name = f"{mode}.log"
        path = out / name
        if path.is_file():
            logs[name] = tail(path)
    report = out / "report.md"
    return 200, {
        "job_id": job_id,
        "out": rel(out),
        "status": status,
        "logs": logs,
        "environment": read_json(out / "environment.json", {}),
        "report_exists": report.is_file(),
        "report_path": rel(report),
        "report_markdown": report.read_text(encoding="utf-8", errors="replace") if report.is_file() else "",
    }


def latest_repro_summaries(limit: int = 6) -> list[dict]:
    if not REPRO_JOB_ROOT.is_dir():
        return []
    paths = sorted(REPRO_JOB_ROOT.glob("**/status.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out = []
    for path in paths[:limit]:
        status = read_json(path, {})
        if status:
            status["_path"] = rel(path)
            out.append(status)
    return out


def latest_repro_summary_for_bug(bug_id: str, root: Optional[Path] = None) -> Optional[dict]:
    repro_root = root or REPRO_JOB_ROOT
    if not repro_root.is_dir():
        return None
    matches = []
    for path in repro_root.glob("**/status.json"):
        status = read_json(path, {})
        if status.get("bug_id") == bug_id:
            matches.append((path.stat().st_mtime, path, status))
    if not matches:
        return None
    _, path, status = max(matches, key=lambda item: item[0])
    status = dict(status)
    status["_path"] = rel(path)
    return status


def repro_conclusion(status: dict) -> str:
    modes = status.get("modes", {})
    finished = [m for m, item in modes.items() if item.get("status") in ("finished", "timeout", "failed")]
    if not finished:
        return "当前环境尚未运行复现。"
    reproduced = []
    not_reproduced = []
    timed_out = []
    needs_review = []
    for mode, item in modes.items():
        verdict = item.get("evidence", {}).get("verdict") or item.get("verdict")
        if verdict == "reproduced":
            reproduced.append(mode)
        elif verdict == "not_reproduced":
            not_reproduced.append(mode)
        elif verdict == "timeout":
            timed_out.append(mode)
        elif verdict == "needs_review":
            needs_review.append(mode)
    parts = []
    if reproduced:
        parts.append(f"{', '.join(reproduced)} 捕获到与规则匹配的崩溃、断言或后端差异证据。")
    if not_reproduced:
        parts.append(f"{', '.join(not_reproduced)} 返回码为 0，当前环境未复现该异常，可能是版本差异或该后端未触发。")
    if timed_out:
        parts.append(f"{', '.join(timed_out)} 超时，需要人工确认。")
    if needs_review:
        parts.append(f"{', '.join(needs_review)} 返回异常但未命中内置判定关键词，需要人工查看日志。")
    return " ".join(parts) if parts else "复现状态无法从当前输出自动判断，请人工查看日志。"


def report_id_for(status: dict) -> str:
    started = str(status.get("started_at", "")).replace("-", "").replace(":", "").replace("T", "-")
    return f"TG-RPT-{display_bug_id(str(status.get('bug_id', 'UNKNOWN')))}-{safe_name(started)}"


def report_execution_table(status: dict) -> list[str]:
    rows = [
        "| 执行配置 | 状态 | 返回码 | 观测类型 | 信号 | 规则结论 | 实际设备 | 耗时 | 判定依据 |",
        "| --- | --- | ---: | --- | --- | --- | --- | ---: | --- |",
    ]
    for mode, item in status.get("modes", {}).items():
        evidence = item.get("evidence") or {}
        signal_name = evidence.get("signal") or "-"
        rows.append(
            "| {profile} | {status} | {returncode} | {outcome} | {signal} | {verdict} | {device} | {elapsed}s | {reason} |".format(
                profile=item.get("execution_profile", mode),
                status=item.get("status", "pending"),
                returncode=item.get("returncode", "-"),
                outcome=evidence.get("outcome", "unclassified"),
                signal=signal_name,
                verdict=evidence.get("verdict", item.get("verdict", "pending")),
                device=item.get("actual_device", "unknown"),
                elapsed=item.get("elapsed_seconds", "-"),
                reason=str(evidence.get("reason", "-")).replace("|", "/"),
            )
        )
    return rows


def report_attachments(status: dict, out: Path) -> list[str]:
    rows = ["| 附件 | SHA-256 |", "| --- | --- |"]
    candidates = [out / "repro.py", out / "environment.json"]
    candidates.extend(out / f"{mode}.log" for mode in status.get("modes", {}))
    for path in candidates:
        if path.is_file():
            rows.append(f"| `{rel(path)}` | `{sha256_file(path)}` |")
    return rows


def generate_repro_report(job_id: str) -> tuple[int, dict]:
    out = find_repro_job(job_id)
    if out is None:
        return 404, {"error": "repro job not found"}
    report_path = out / "report.md"
    if report_path.is_file():
        return 200, {
            "job_id": job_id,
            "report_path": rel(report_path),
            "report_markdown": report_path.read_text(encoding="utf-8", errors="replace"),
            "immutable": True,
        }
    status = read_json(out / "status.json", {})
    if status.get("status") != "finished":
        return 409, {"error": "reproduction must finish before report generation"}
    bug_id = status.get("bug_id", "")
    detail_code, detail = paper_bug_detail(bug_id)
    if detail_code != 200:
        return detail_code, detail
    meta = detail["meta"]
    environment = read_json(out / "environment.json", {})
    report_id = report_id_for(status)
    lines = [
        f"# TensorGuard 复现证据报告 {display_bug_id(bug_id)}",
        "",
        "## 报告摘要",
        "",
        f"- 报告编号：`{report_id}`",
        f"- 问题编号：`{display_bug_id(bug_id)}`",
        f"- API：`{meta.get('api', '')}`",
        f"- 框架：`{meta.get('framework', '')}`",
        f"- 问题类型：`{meta.get('bug_type', '')}`",
        f"- 生成时间：`{now()}`",
        "",
        "## 当前复现结论",
        "",
        repro_conclusion(status),
        "",
        "> 本结论由退出码、POSIX 信号和明确日志模式确定性生成，只描述本次运行证据，不推断根因、可利用性或风险等级。",
        "",
        "## 预期与观测",
        "",
        f"**预期行为**：{meta.get('expected', '')}",
        "",
        f"**已知观测**：{meta.get('observed', '')}",
        "",
        "## 本次执行证据",
        "",
        *report_execution_table(status),
        "",
        "## 最小复现代码",
        "",
        "```python",
        detail.get("repro_code", "").rstrip(),
        "```",
        "",
        "## 输出摘录",
        "",
    ]
    for mode in status.get("modes", {}):
        lines.extend(
            [
                f"### {status['modes'][mode].get('execution_profile', mode)}",
                "",
                "```text",
                tail(out / f"{mode}.log", max_chars=6000).rstrip(),
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## 环境快照",
            "",
            "```json",
            json.dumps(environment, ensure_ascii=False, indent=2),
            "```",
            "",
            "## 证据附件",
            "",
            *report_attachments(status, out),
            "",
            "## 适用边界",
            "",
            "- 该报告只证明所列环境与执行配置下捕获到的行为。",
            "- `CUDA_VISIBLE_DEVICES` 仅代表可见设备配置；除非复现程序自行打印设备，否则实际执行设备记为 `unknown`。",
            "- 自动规则不会判断根因、漏洞可利用性、CVSS 或严重程度；这些结论需要框架维护者或人工源码审查。",
            "- 首次生成后报告保持不变；后续复现会创建新的证据记录。",
            "",
        ]
    )
    report = "\n".join(lines).rstrip() + "\n"
    report = write_report_once(report_path, report)
    status["report_id"] = report_id
    status["report"] = rel(report_path)
    status["updated_at"] = now()
    write_json(out / "status.json", status)
    return 200, {
        "job_id": job_id,
        "report_path": rel(report_path),
        "report_markdown": report,
        "immutable": True,
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "TensorGuardDemo/0.2"

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/":
            self.serve_static("index.html")
            return
        if path.startswith("/static/"):
            self.serve_static(path[len("/static/") :])
            return
        if path == "/api/overview":
            send_json(self, overview_payload())
            return
        if path == "/api/environment":
            force = query.get("refresh", ["0"])[0] == "1"
            send_json(self, environment_payload(force=force))
            return
        if path == "/api/apis":
            self.api_apis(query)
            return
        if path == "/api/candidates":
            send_json(self, CANDIDATE_STORE.list())
            return
        if path == "/api/candidate-clusters":
            status, payload = candidate_clusters_payload()
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/candidate-clusters/"):
            status, payload = candidate_cluster_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/candidate-validation-jobs/"):
            status, payload = candidate_validation_job_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/candidates/"):
            status, payload = candidate_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path == "/api/api-detail":
            self.api_api_detail(query)
            return
        if path.startswith("/api/api-jobs/") and "/logs/" in path:
            parts = path.split("/")
            if len(parts) != 6 or parts[4] != "logs":
                send_json(self, {"error": "invalid API job log path"}, status=400)
                return
            try:
                offset = int(query.get("offset", ["0"])[0])
            except (TypeError, ValueError):
                send_json(self, {"error": "offset must be a non-negative integer"}, status=400)
                return
            status, payload = api_job_log_chunk(unquote(parts[3]), unquote(parts[5]), offset)
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/api-jobs/"):
            status, payload = api_job_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path in ("/api/confirmed-bugs", "/api/paper-bugs"):
            send_json(self, load_paper_bugs())
            return
        if path.startswith("/api/confirmed-bugs/") or path.startswith("/api/paper-bugs/"):
            status, payload = paper_bug_detail(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/repro-jobs/") and path.endswith("/report"):
            job_id = unquote(path.split("/")[-2])
            status, payload = generate_repro_report(job_id)
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/repro-jobs/"):
            status, payload = repro_job_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        send_json(self, {"error": "not found"}, status=404)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        ok, payload = read_body(self)
        if not ok:
            send_json(self, payload, status=400)
            return
        if parsed.path == "/api/run-api":
            status, response = start_api_job(payload)
            send_json(self, response, status=status)
            return
        if parsed.path == "/api/candidates":
            status, response = create_candidate(payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/confirm"):
            cluster_id = unquote(parsed.path.split("/")[-2])
            status, response = confirm_candidate_cluster(cluster_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/delete"):
            cluster_id = unquote(parsed.path.split("/")[-2])
            status, response = delete_candidate_cluster(cluster_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/status"):
            cluster_id = unquote(parsed.path.split("/")[-2])
            status, response = update_candidate_cluster(cluster_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/draft/reset"):
            cluster_id = unquote(parsed.path.split("/")[-3])
            status, response = reset_candidate_cluster_draft(cluster_id)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/draft"):
            cluster_id = unquote(parsed.path.split("/")[-2])
            status, response = save_candidate_cluster_draft(cluster_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidate-clusters/") and parsed.path.endswith("/validate"):
            cluster_id = unquote(parsed.path.split("/")[-2])
            status, response = start_candidate_validation(cluster_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/candidates/") and parsed.path.endswith("/status"):
            candidate_id = unquote(parsed.path.split("/")[-2])
            status, response = update_candidate(candidate_id, payload)
            send_json(self, response, status=status)
            return
        if (parsed.path.startswith("/api/confirmed-bugs/") or parsed.path.startswith("/api/paper-bugs/")) and parsed.path.endswith("/reproduce"):
            bug_id = unquote(parsed.path.split("/")[-2])
            status, response = start_repro_job(bug_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/confirmed-bugs/") and parsed.path.endswith("/delete"):
            bug_id = unquote(parsed.path.split("/")[-2])
            status, response = delete_confirmed_bug(bug_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/repro-jobs/") and parsed.path.endswith("/report"):
            job_id = unquote(parsed.path.split("/")[-2])
            status, response = generate_repro_report(job_id)
            send_json(self, response, status=status)
            return
        send_json(self, {"error": "not found"}, status=404)

    def serve_static(self, name: str) -> None:
        clean = Path(name)
        if clean.is_absolute() or ".." in clean.parts:
            send_json(self, {"error": "invalid static path"}, status=400)
            return
        path = STATIC_ROOT / clean
        if not path.is_file():
            send_json(self, {"error": "static file not found"}, status=404)
            return
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        write_response(self, 200, path.read_bytes(), content_type)

    def api_apis(self, query: dict) -> None:
        lib = query.get("lib", ["torch"])[0]
        q = query.get("q", [""])[0]
        limit_raw = query.get("limit", ["200"])[0]
        try:
            limit = max(1, min(int(limit_raw), 5000))
        except ValueError:
            limit = 200
        if lib not in ("torch", "tf"):
            send_json(self, {"error": "lib must be torch or tf"}, status=400)
            return
        send_json(self, api_list_payload(lib, q, limit=limit))

    def api_api_detail(self, query: dict) -> None:
        lib = query.get("lib", ["torch"])[0]
        api = query.get("api", [""])[0]
        status, payload = api_detail_payload(lib, api)
        send_json(self, payload, status=status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the TensorGuard demo workbench.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8008)
    args = parser.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"TensorGuard Demo: http://{args.host}:{args.port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
