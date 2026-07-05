"""Validation helpers for the curated confirmed-bug index."""

from __future__ import annotations

import json
import os
import re
import shutil
import threading
from datetime import datetime
from pathlib import Path


def _read_object(path: Path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value


def load_confirmed_records(index_path: Path, repo_root: Path) -> list[dict]:
    index = _read_object(index_path)
    if not isinstance(index, list):
        return []
    root = repo_root.resolve()
    records = []
    for raw in index:
        if not isinstance(raw, dict) or not raw.get("id") or not raw.get("path"):
            continue
        meta_path = (root / str(raw["path"])).resolve()
        if not meta_path.is_relative_to(root) or not meta_path.is_file():
            continue
        meta = _read_object(meta_path)
        if not isinstance(meta, dict) or meta.get("id") != raw.get("id"):
            continue
        repro_name = str(meta.get("files", {}).get("repro", "repro.py"))
        repro_path = (meta_path.parent / repro_name).resolve()
        if not repro_path.is_relative_to(meta_path.parent.resolve()) or not repro_path.is_file():
            continue
        record = {**raw, **meta}
        record.pop("severity", None)
        records.append(record)
    return records


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:64] or "bug"


class DynamicConfirmedBugStore:
    """Mutable confirmed-Bug archive; curated baseline records remain separate."""

    def __init__(self, repo_root: Path, store_root: Path | None = None) -> None:
        self.repo_root = repo_root.resolve()
        self.root = (store_root or self.repo_root / "demo_runs" / "confirmed_bugs").resolve()
        self.index_path = self.root / "index.json"
        self._lock = threading.Lock()

    def _read_index(self) -> list[dict]:
        value = _read_object(self.index_path)
        return value if isinstance(value, list) else []

    def _write_index(self, records: list[dict]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        tmp = self.index_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(tmp, self.index_path)

    def list(self) -> list[dict]:
        return load_confirmed_records(self.index_path, self.repo_root)

    def get(self, bug_id: str) -> dict | None:
        return next((item for item in self.list() if item.get("id") == bug_id), None)

    def _next_id(self, records: list[dict]) -> str:
        numbers = []
        for item in records:
            match = re.fullmatch(r"BUG-(\d+)", str(item.get("id", "")))
            if match:
                numbers.append(int(match.group(1)))
        return f"BUG-{max(numbers, default=0) + 1:04d}"

    def archive_candidate(
        self,
        *,
        cluster: dict,
        repro_path: Path,
        validation_dir: Path,
        environment: dict,
        review_metadata: dict | None = None,
    ) -> dict:
        if not repro_path.is_file():
            raise ValueError("saved repro.py is required")
        status_path = validation_dir / "status.json"
        validation = _read_object(status_path)
        if not isinstance(validation, dict) or validation.get("status") != "finished":
            raise ValueError("a finished CPU/GPU validation is required")
        cluster_id = str(cluster.get("cluster_id", ""))
        if not cluster_id:
            raise ValueError("candidate cluster id is required")

        with self._lock:
            records = self._read_index()
            existing = next((item for item in records if item.get("candidate_cluster_id") == cluster_id), None)
            if existing:
                loaded = self.get(str(existing.get("id", "")))
                if loaded is not None:
                    return loaded
            bug_id = self._next_id(records)
            api = str(cluster.get("api", "unknown"))
            pattern = str(cluster.get("bug_pattern", "framework behavior inconsistency"))
            review = review_metadata or {}
            title = str(review.get("title") or f"{api} · {pattern}")
            bug_type = str(review.get("bug_type") or pattern)
            review_note = str(review.get("review_note") or pattern)
            lib = str(cluster.get("lib", ""))
            framework = "PyTorch" if lib == "torch" else "TensorFlow" if lib == "tf" else lib
            bug_dir = self.root / f"{bug_id}-{_slug(api)}"
            bug_dir.mkdir(parents=True, exist_ok=False)
            shutil.copy2(repro_path, bug_dir / "repro.py")
            evidence_dir = bug_dir / "evidence"
            evidence_dir.mkdir()
            for name in ("cpu.log", "gpu0.log", "status.json"):
                source = validation_dir / name
                if source.is_file():
                    shutil.copy2(source, evidence_dir / name)
            (bug_dir / "environment.json").write_text(
                json.dumps(environment, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            meta = {
                "id": bug_id,
                "title": title,
                "framework": framework,
                "api": api,
                "related_apis": [],
                "bug_type": bug_type,
                "status": "confirmed",
                "source": {"document": "TensorGuard candidate review", "section": cluster_id},
                "trigger": "Execute the archived repro.py in the recorded environment.",
                "expected": "The framework should handle the input consistently without an internal crash or backend mismatch.",
                "observed": pattern,
                "review_note": review_note,
                "reproducible": True,
                "minimized": True,
                "files": {"repro": "repro.py", "report": "report.md"},
                "tags": [lib, str(cluster.get("category", "candidate")), "candidate-confirmed"],
                "dynamic": True,
                "candidate_cluster_id": cluster_id,
                "validation_run_id": validation.get("run_id"),
                "confirmed_at": _now(),
            }
            (bug_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            report = (
                f"# {bug_id}: {title}\n\n"
                f"## Confirmation\n\n- Type: {bug_type}\n- Pattern: {pattern}\n- Candidate: `{cluster_id}`\n"
                f"- Validation: `{validation.get('run_id', '')}`\n\n"
                f"## Human review\n\n{review_note}\n\n"
                "## Evidence\n\nSee `repro.py`, `environment.json`, and `evidence/`.\n"
            )
            (bug_dir / "report.md").write_text(report, encoding="utf-8")
            relative_meta = (bug_dir / "meta.json").relative_to(self.repo_root).as_posix()
            index_record = {
                "id": bug_id,
                "framework": framework,
                "api": api,
                "title": meta["title"],
                "bug_type": bug_type,
                "status": "confirmed",
                "path": relative_meta,
                "dynamic": True,
                "candidate_cluster_id": cluster_id,
            }
            records.append(index_record)
            self._write_index(records)
        loaded = self.get(bug_id)
        if loaded is None:
            raise RuntimeError("confirmed Bug archive could not be reloaded")
        return loaded

    def delete(self, bug_id: str, *, confirmation_id: str) -> None:
        if confirmation_id != bug_id:
            raise ValueError("confirmation id does not match Bug ID")
        with self._lock:
            records = self._read_index()
            record = next((item for item in records if item.get("id") == bug_id), None)
            if record is None:
                raise KeyError(bug_id)
            meta_path = (self.repo_root / str(record.get("path", ""))).resolve()
            if not meta_path.is_relative_to(self.root) or meta_path.name != "meta.json":
                raise ValueError("confirmed Bug path is outside the dynamic archive")
            self._write_index([item for item in records if item.get("id") != bug_id])
            shutil.rmtree(meta_path.parent, ignore_errors=False)
