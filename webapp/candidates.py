"""Persistent review-candidate index backed by immutable API job files."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import threading
from datetime import datetime
from pathlib import Path
from typing import Optional


ALLOWED_CATEGORIES = {"seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"}
ALLOWED_STATES = {"pending_review", "reproduced", "needs_review", "rejected", "promoted"}
RECOMMEND_PATTERNS = (
    "internal assert",
    "check failed",
    "fatal",
    "device-side assert",
    "segmentation fault",
    "floating point exception",
    "double free",
    "invalid pointer",
    "invalid next size",
    "cpu/gpu",
    "varinconsistentcatch",
    "comparisonfail",
    "frameworkcrashcatch",
    "timeoutfail",
)
NOISE_PATTERNS = (
    ("syntax_error", "syntaxerror"),
    ("name_error", "nameerror"),
    ("import_error", "importerror"),
    ("missing_module", "modulenotfounderror"),
    ("generated_code_error", "unterminated triple-quoted string"),
    ("generated_code_error", "was never closed"),
    ("generated_code_error", "unexpected eof"),
    ("undefined_framework", "name 'torch' is not defined"),
    ("undefined_framework", "name 'tf' is not defined"),
)
CATEGORY_PRIORITY = {"crash": 100, "hangs": 90, "exception": 70, "seed": 60, "valid": 55, "flaky": 45, "notarget": 25}
MAX_DRAFT_BYTES = 200_000


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def recommend_candidate(category: str, evidence: str) -> bool:
    if category in {"crash", "hangs"}:
        return True
    lowered = evidence.lower()
    if any(pattern in lowered for pattern in RECOMMEND_PATTERNS):
        return True
    return False


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")[:64] or "unknown"


def _next_candidate_id(records: list[dict]) -> str:
    numbers = []
    for record in records:
        match = re.fullmatch(r"CAND-(\d+)", str(record.get("id", "")))
        if match:
            numbers.append(int(match.group(1)))
    return f"CAND-{max(numbers, default=0) + 1:04d}"


def _noise_reason(evidence: str) -> Optional[str]:
    lowered = evidence.lower()
    for reason, pattern in NOISE_PATTERNS:
        if pattern in lowered:
            return reason
    return None


def _bug_pattern(category: str, evidence: str) -> str:
    lowered = evidence.lower()
    has_cuda_assert = "device-side assert" in lowered or "cudaerrorassert" in lowered
    has_cpu_gpu = "cpu" in lowered and "gpu" in lowered
    if has_cuda_assert:
        return "CPU/GPU exception mismatch / CUDA device-side assert"
    if "internal assert" in lowered or "check failed" in lowered:
        return "Internal assert / framework invariant failure"
    if any(pattern in lowered for pattern in ("invalid pointer", "invalid next size", "double free", "segmentation fault", "free():")):
        return "Crash / memory corruption"
    if "varinconsistentcatch" in lowered or "comparisonfail" in lowered or "cpu/gpu" in lowered:
        return "CPU/GPU value inconsistency"
    if category == "hangs":
        return "Hang / timeout"
    if category == "crash":
        return "Crash / process abort"
    return f"{category} / manual review"


def review_defaults(cluster: dict) -> dict:
    api = str(cluster.get("api", "unknown"))
    pattern = str(cluster.get("bug_pattern", "framework behavior inconsistency"))
    lowered = pattern.lower()
    if "device-side assert" in lowered:
        bug_type = "CUDA device-side assert"
    elif "memory corruption" in lowered or "invalid pointer" in lowered:
        bug_type = "Memory corruption / invalid free / out-of-bounds"
    elif "internal assert" in lowered or "invariant" in lowered:
        bug_type = "Internal assertion failure"
    elif "hang" in lowered or "timeout" in lowered:
        bug_type = "Hang / timeout / deadlock"
    elif "exception mismatch" in lowered:
        bug_type = "CPU/GPU exception mismatch"
    elif "value inconsistency" in lowered or "comparison" in lowered:
        bug_type = "CPU/GPU value mismatch"
    elif "crash" in lowered or "abort" in lowered:
        bug_type = "Process crash / abnormal exit"
    else:
        bug_type = pattern
    return {
        "title": f"{api} · {pattern}",
        "bug_type": bug_type,
        "review_note": f"已完成 {api} 的候选代码检查与 CPU/GPU 独立进程复现，等待人工确认框架缺陷结论。",
    }


def _cluster_status(records: list[dict]) -> str:
    statuses = {str(record.get("status", "")) for record in records}
    if "promoted" in statuses:
        return "promoted"
    if statuses and statuses <= {"rejected"}:
        return "rejected"
    if "reproduced" in statuses:
        return "needs_minimize"
    if "needs_review" in statuses:
        return "needs_review"
    return "needs_minimize"


def _candidate_score(record: dict) -> float:
    category = str(record.get("category", ""))
    score = float(CATEGORY_PRIORITY.get(category, 0))
    if record.get("recommended"):
        score += 25.0
    source_path = str(record.get("source_path", ""))
    try:
        score += max(0.0, 10.0 - (len(source_path) / 100.0))
    except TypeError:
        pass
    evidence = str(record.get("error_summary", ""))
    if "device-side assert" in evidence.lower() or "internal assert" in evidence.lower():
        score += 5.0
    return round(score, 3)


def _member_payload(record: dict) -> dict:
    source_path = str(record.get("source_path", ""))
    return {
        "candidate_id": record.get("id", ""),
        "source_path": source_path,
        "source_name": Path(source_path).name,
        "error_summary": str(record.get("error_summary", "")),
        "score": _candidate_score(record),
        "status": record.get("status", "pending_review"),
    }


def _trace_entries(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    headers = list(
        re.finditer(
            r"^Testcase\s+\d+\s+(?P<api>\S+)\s+(?P<label>\S+)\s+(?P<reason>\S+)(?P<tail>[^\n]*)",
            text,
            flags=re.MULTILINE,
        )
    )
    entries = []
    for index, header in enumerate(headers):
        end = headers[index + 1].start() if index + 1 < len(headers) else len(text)
        block = text[header.start():end].strip()
        entries.append(
            {
                "api": header.group("api"),
                "label": header.group("label"),
                "reason": header.group("reason"),
                "evidence": block[:8000],
            }
        )
    return entries


class CandidateStore:
    def __init__(self, repo_root: Path, index_path: Optional[Path] = None) -> None:
        self.repo_root = repo_root.resolve()
        self.jobs_root = (self.repo_root / "demo_runs" / "api_jobs").resolve()
        self.index_path = index_path or self.repo_root / "demo_runs" / "candidates" / "index.json"
        self._lock = threading.Lock()

    def _cluster_workspace(self, cluster_id: str) -> Path:
        digest = hashlib.sha256(cluster_id.encode("utf-8")).hexdigest()[:20]
        return self.index_path.parent / "workspaces" / digest

    def _write_workspace_file(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(content, encoding="utf-8")
        os.replace(tmp, path)

    def _write_workspace_metadata(self, workspace: Path, payload: dict) -> None:
        self._write_workspace_file(
            workspace / "metadata.json",
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        )

    def _read(self) -> list[dict]:
        if not self.index_path.is_file():
            return []
        try:
            data = json.loads(self.index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return []
        return data if isinstance(data, list) else []

    def _write(self, records: list[dict]) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.index_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(tmp, self.index_path)

    def list(self) -> list[dict]:
        return sorted(self._read(), key=lambda item: item.get("created_at", ""), reverse=True)

    def get(self, candidate_id: str) -> Optional[dict]:
        return next((item for item in self._read() if item.get("id") == candidate_id), None)

    def _cluster_groups(self) -> tuple[dict[str, list[dict]], list[dict]]:
        groups: dict[str, list[dict]] = {}
        excluded: list[dict] = []
        for record in self.list():
            evidence = str(record.get("error_summary", ""))
            reason = _noise_reason(evidence)
            if reason is None and not record.get("recommended"):
                reason = "low_signal_non_framework_error"
            if reason is not None:
                excluded.append({**_member_payload(record), "reason": reason})
                continue
            category = str(record.get("category", ""))
            pattern = _bug_pattern(category, evidence)
            key = "|".join(
                [
                    str(record.get("lib", "")),
                    str(record.get("api", "")),
                    category,
                    pattern,
                ]
            )
            groups.setdefault(key, []).append({**record, "_bug_pattern": pattern})
        return groups, excluded

    def _cluster_summary(self, key: str, records: list[dict], excluded: list[dict]) -> dict:
        representative = max(records, key=_candidate_score)
        lib, api, category, pattern = key.split("|", 3)
        api_excluded = [
            item
            for item in excluded
            if item.get("source_name", "").startswith(f"{api.rsplit('.', 1)[-1]}_") or str(item.get("source_path", "")).find(f"/{api}_") >= 0
        ]
        latest = max(str(record.get("updated_at", record.get("created_at", ""))) for record in records)
        earliest = min(str(record.get("created_at", "")) for record in records)
        return {
            "cluster_id": f"{_slug(lib)}_{_slug(api)}_{_slug(category)}_{_slug(pattern)}",
            "lib": lib,
            "api": api,
            "job_id": representative.get("job_id", ""),
            "category": category,
            "bug_pattern": pattern,
            "cluster_status": _cluster_status(records),
            "confidence": "high" if len(records) > 1 or representative.get("recommended") else "medium",
            "member_count": len(records),
            "excluded_count": len(api_excluded),
            "representative": _member_payload(representative),
            "created_at": earliest,
            "updated_at": latest,
        }

    def list_clusters(self) -> list[dict]:
        groups, excluded = self._cluster_groups()
        clusters = [self._cluster_summary(key, records, excluded) for key, records in groups.items()]
        visible = [item for item in clusters if item.get("cluster_status") != "promoted"]
        return sorted(visible, key=lambda item: (item.get("confidence") != "high", item.get("updated_at", "")), reverse=True)

    def get_cluster(self, cluster_id: str) -> Optional[dict]:
        groups, excluded = self._cluster_groups()
        for key, records in groups.items():
            summary = self._cluster_summary(key, records, excluded)
            if summary.get("cluster_id") != cluster_id:
                continue
            member_payloads = sorted((_member_payload(record) for record in records), key=lambda item: item["score"], reverse=True)
            representative = summary["representative"]
            source = self.repo_root / str(representative.get("source_path", ""))
            summary["members"] = member_payloads
            summary["excluded"] = [
                item
                for item in excluded
                if str(item.get("source_path", "")).startswith(f"demo_runs/api_jobs/{summary['job_id']}/")
                and f"/{summary['category']}/" in str(item.get("source_path", ""))
            ]
            summary["representative_source_code"] = source.read_text(encoding="utf-8", errors="replace") if source.is_file() else ""
            workspace = self._cluster_workspace(cluster_id)
            draft_path = workspace / "repro.py"
            draft_saved = draft_path.is_file()
            draft = draft_path.read_text(encoding="utf-8", errors="replace") if draft_saved else summary["representative_source_code"]
            summary["minimization_draft"] = draft
            summary["draft_saved"] = draft_saved
            summary["draft_modified"] = draft != summary["representative_source_code"]
            summary["draft_sha256"] = hashlib.sha256(draft.encode("utf-8")).hexdigest() if draft else ""
            summary["review_defaults"] = review_defaults(summary)
            return summary
        return None

    def save_cluster_draft(self, cluster_id: str, source: str) -> dict:
        cluster = self.get_cluster(cluster_id)
        if cluster is None:
            raise KeyError(cluster_id)
        if not isinstance(source, str):
            raise ValueError("candidate draft must be text")
        encoded = source.encode("utf-8")
        if not source.strip():
            raise ValueError("candidate draft cannot be empty")
        if len(encoded) > MAX_DRAFT_BYTES:
            raise ValueError(f"candidate draft exceeds {MAX_DRAFT_BYTES} bytes")
        workspace = self._cluster_workspace(cluster_id)
        with self._lock:
            self._write_workspace_file(workspace / "repro.py", source)
            self._write_workspace_metadata(
                workspace,
                {
                    "cluster_id": cluster_id,
                    "draft_sha256": hashlib.sha256(encoded).hexdigest(),
                    "updated_at": now(),
                },
            )
        updated = self.get_cluster(cluster_id)
        if updated is None:
            raise KeyError(cluster_id)
        return updated

    def reset_cluster_draft(self, cluster_id: str) -> dict:
        cluster = self.get_cluster(cluster_id)
        if cluster is None:
            raise KeyError(cluster_id)
        return self.save_cluster_draft(cluster_id, cluster["representative_source_code"])

    def cluster_draft_path(self, cluster_id: str) -> Path:
        cluster = self.get_cluster(cluster_id)
        if cluster is None:
            raise KeyError(cluster_id)
        if not cluster["draft_saved"]:
            self.save_cluster_draft(cluster_id, cluster["minimization_draft"])
        return self._cluster_workspace(cluster_id) / "repro.py"

    def cluster_workspace_path(self, cluster_id: str) -> Path:
        if self.get_cluster(cluster_id) is None:
            raise KeyError(cluster_id)
        return self._cluster_workspace(cluster_id)

    def delete_cluster(self, cluster_id: str, *, confirmation_id: str) -> None:
        if confirmation_id != cluster_id:
            raise ValueError("confirmation id does not match candidate cluster ID")
        cluster = self.get_cluster(cluster_id)
        if cluster is None:
            raise KeyError(cluster_id)
        member_ids = {member.get("candidate_id") for member in cluster.get("members", [])}
        workspace = self._cluster_workspace(cluster_id)
        with self._lock:
            records = self._read()
            self._write([record for record in records if record.get("id") not in member_ids])
        if workspace.is_dir():
            shutil.rmtree(workspace)

    def _validated_source(
        self,
        job_id: str,
        lib: str,
        api: str,
        category: str,
        source_path: Path,
    ) -> Path:
        if lib not in {"torch", "tf"}:
            raise ValueError("lib must be torch or tf")
        if category not in ALLOWED_CATEGORIES:
            raise ValueError("unsupported candidate category")
        source = source_path.resolve()
        if not source.is_file() or source.suffix != ".py":
            raise ValueError("candidate source must be an existing .py file")
        if not source.is_relative_to(self.jobs_root):
            raise ValueError("candidate source must be inside demo_runs/api_jobs")
        expected_root = self.jobs_root / job_id / "Results" / lib / category
        if not source.is_relative_to(expected_root.resolve()):
            raise ValueError("candidate source does not match job, library, or category")
        if source.stem.rsplit("_", 1)[0] != api:
            raise ValueError("candidate source does not match API")
        return source

    def add(
        self,
        *,
        job_id: str,
        lib: str,
        api: str,
        category: str,
        source_path: Path,
        note: str = "",
        evidence: Optional[str] = None,
    ) -> dict:
        source = self._validated_source(job_id, lib, api, category, source_path)
        source_hash = sha256_file(source)
        evidence_text = (evidence if evidence is not None else source.read_text(encoding="utf-8", errors="replace"))[:8000]
        with self._lock:
            records = self._read()
            existing = next(
                (
                    item
                    for item in records
                    if item.get("api") == api and item.get("source_sha256") == source_hash
                ),
                None,
            )
            if existing:
                return existing
            record = {
                "id": _next_candidate_id(records),
                "job_id": job_id,
                "lib": lib,
                "api": api,
                "category": category,
                "source_path": source.relative_to(self.repo_root).as_posix(),
                "source_sha256": source_hash,
                "status": "pending_review",
                "recommended": recommend_candidate(category, evidence_text),
                "error_summary": evidence_text[:2000],
                "note": note.strip(),
                "created_at": now(),
                "updated_at": now(),
            }
            records.append(record)
            self._write(records)
            return record

    def collect_job_results(self, *, job_id: str, lib: str, api: str) -> dict:
        if lib not in {"torch", "tf"}:
            raise ValueError("lib must be torch or tf")
        job_root = self.jobs_root / job_id
        results_root = job_root / "Results" / lib
        report = {
            "job_id": job_id,
            "lib": lib,
            "api": api,
            "scanned": 0,
            "registered": 0,
            "deduplicated": 0,
            "excluded_noise": 0,
            "skipped_low_signal": 0,
            "candidate_ids": [],
        }
        if not results_root.is_dir():
            return report

        existing_ids = {str(record.get("id", "")) for record in self.list()}
        considered_sources: set[Path] = set()

        def consider(source: Path, category: str, evidence: str) -> None:
            resolved = source.resolve()
            if resolved in considered_sources:
                return
            considered_sources.add(resolved)
            report["scanned"] += 1
            if _noise_reason(evidence) is not None:
                report["excluded_noise"] += 1
                return
            if not recommend_candidate(category, evidence):
                report["skipped_low_signal"] += 1
                return
            record = self.add(
                job_id=job_id,
                lib=lib,
                api=api,
                category=category,
                source_path=source,
                note="Automatically collected after single-API run",
                evidence=evidence,
            )
            candidate_id = str(record.get("id", ""))
            report["candidate_ids"].append(candidate_id)
            if candidate_id in existing_ids:
                report["deduplicated"] += 1
            else:
                report["registered"] += 1
                existing_ids.add(candidate_id)

        category_order = ("crash", "hangs", "exception", "valid", "seed", "flaky", "notarget")
        for entry in _trace_entries(results_root / "trace.txt"):
            if entry["api"] != api:
                continue
            source = None
            category = ""
            for candidate_category in category_order:
                candidate_source = results_root / candidate_category / f"{entry['label']}.py"
                if candidate_source.is_file():
                    source = candidate_source
                    category = candidate_category
                    break
            if source is not None:
                consider(source, category, entry["evidence"])

        for category in ("crash", "hangs", "exception"):
            folder = results_root / category
            if not folder.is_dir():
                continue
            for source in sorted(folder.glob("*.py")):
                if source.stem.rsplit("_", 1)[0] != api:
                    continue
                evidence = source.read_text(encoding="utf-8", errors="replace")[:8000]
                consider(source, category, evidence)

        report["candidate_ids"] = list(dict.fromkeys(report["candidate_ids"]))
        return report

    def update_status(self, candidate_id: str, status: str, note: Optional[str] = None) -> dict:
        if status not in ALLOWED_STATES:
            raise ValueError("unsupported candidate status")
        with self._lock:
            records = self._read()
            record = next((item for item in records if item.get("id") == candidate_id), None)
            if record is None:
                raise KeyError(candidate_id)
            record["status"] = status
            if note is not None:
                record["note"] = note.strip()
            record["updated_at"] = now()
            self._write(records)
            return record

    def update_cluster_status(self, cluster_id: str, status: str, note: Optional[str] = None) -> dict:
        if status not in ALLOWED_STATES:
            raise ValueError("unsupported candidate status")
        cluster = self.get_cluster(cluster_id)
        if cluster is None:
            raise KeyError(cluster_id)
        member_ids = {member.get("candidate_id") for member in cluster.get("members", [])}
        with self._lock:
            records = self._read()
            for record in records:
                if record.get("id") not in member_ids:
                    continue
                record["status"] = status
                if note is not None:
                    record["note"] = note.strip()
                record["updated_at"] = now()
            self._write(records)
        updated = self.get_cluster(cluster_id)
        if updated is None:
            raise KeyError(cluster_id)
        return updated
