#!/usr/bin/env python3
"""Run one API through the TensorGuard demo pipeline.

Pipeline:
  prompt library check -> qwen_seed.py -> ev_generation.py -> driver.py

The script is intentionally a thin wrapper. It does not change the
generation or oracle logic; it only gives the competition demo a stable
one-command entrypoint and structured outputs.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.demo_metrics import append_metric, build_metric  # noqa: E402
from webapp.candidates import CandidateStore  # noqa: E402
from webapp.runtime_data import collect_environment, collect_gpu_sample  # noqa: E402


STAGE_ORDER = ["prompt_check", "qwen_seed", "ev_generation", "driver", "summary"]
RESULT_SUBDIRS = ("seed", "valid", "exception", "crash", "notarget", "hangs", "flaky")
TRACE_PATTERNS = (
    "Catch",
    "Fail",
    "INTERNAL ASSERT",
    "device-side assert",
    "invalid argument",
    "Segmentation fault",
    "free()",
)


def now() -> str:
    return _dt.datetime.now().isoformat(timespec="seconds")


def safe_name(value: str) -> str:
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", value)
    return name.strip("._") or "api"


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def count_py(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for p in path.iterdir() if p.is_file() and p.suffix == ".py")


def read_tail(path: Path, max_chars: int = 4000) -> str:
    if not path.is_file():
        return ""
    data = path.read_bytes()
    return data[-max_chars:].decode("utf-8", errors="replace")


def count_trace_hits(trace_path: Path) -> int:
    if not trace_path.is_file():
        return 0
    count = 0
    with trace_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if any(pattern in line for pattern in TRACE_PATTERNS):
                count += 1
    return count


def mode_defaults(mode: str) -> dict:
    if mode == "demo":
        return {
            "qwen_n_samples": 5,
            "qwen_min_valid": 2,
            "qwen_max_rounds": 1,
            "qwen_per_api_budget": 300,
            "qwen_validate_timeout": 30,
            "ev_max_valid": 5,
            "ev_batch_size": 1,
            "ev_timeout": 300,
        }
    return {
        "qwen_n_samples": 10,
        "qwen_min_valid": 5,
        "qwen_max_rounds": 2,
        "qwen_per_api_budget": 600,
        "qwen_validate_timeout": 30,
        "ev_max_valid": 200,
        "ev_batch_size": 100,
        "ev_timeout": 1000,
    }


class DemoRun:
    def __init__(self, args: argparse.Namespace, repo_root: Path) -> None:
        self.args = args
        self.repo_root = repo_root
        self.out = Path(args.out)
        if not self.out.is_absolute():
            self.out = repo_root / self.out
        self.logs = self.out / "logs"
        self.status_path = self.out / "status.json"
        self.summary_json_path = self.out / "summary.json"
        self.summary_md_path = self.out / "summary.md"
        self.metrics_path = self.out / "metrics.jsonl"
        self.environment_path = self.out / "environment.json"
        self.candidate_collection_path = self.out / "candidate_collection.json"
        self.qwen_out = self.out / "qwen_seed"
        self.results_root = self.out / "Results" / args.lib
        self.canonical_results_root = repo_root / "Results" / args.lib
        self.status = {
            "job_id": args.job_id,
            "lib": args.lib,
            "api": args.api,
            "mode": args.mode,
            "dry_run": args.dry_run,
            "mutation_model": args.mut_model,
            "qwen_model": args.qwen_model,
            "cuda_device": str(args.cuda_device),
            "parameters": {
                "qwen_n_samples": args.qwen_n_samples,
                "qwen_min_valid": args.qwen_min_valid,
                "qwen_max_rounds": args.qwen_max_rounds,
                "qwen_per_api_budget": args.qwen_per_api_budget,
                "qwen_validate_timeout": args.qwen_validate_timeout,
                "ev_max_valid": args.ev_max_valid,
                "ev_batch_size": args.ev_batch_size,
                "ev_timeout": args.ev_timeout,
                "seed_pool_size": args.seed_pool_size,
                "random_seed": args.random_seed,
            },
            "metrics_path": rel(self.metrics_path, self.repo_root),
            "environment_path": rel(self.environment_path, self.repo_root),
            "status": "pending",
            "stage": "init",
            "started_at": now(),
            "updated_at": now(),
            "stages": {stage: "pending" for stage in STAGE_ORDER},
            "logs": {},
            "error": None,
        }

    def update_stage(self, stage: str, state: str, error: Optional[str] = None) -> None:
        self.status["stage"] = stage
        self.status["status"] = "failed" if state == "failed" else "running"
        self.status["stages"][stage] = state
        self.status["updated_at"] = now()
        if error:
            self.status["error"] = error
        write_json(self.status_path, self.status)

    def finish(self, state: str, error: Optional[str] = None) -> None:
        self.status["status"] = state
        self.status["stage"] = "done" if state == "success" else self.status.get("stage")
        self.status["updated_at"] = now()
        if error:
            self.status["error"] = error
        try:
            collection = CandidateStore(self.repo_root).collect_job_results(
                job_id=self.args.job_id,
                lib=self.args.lib,
                api=self.args.api,
            )
            write_json(self.candidate_collection_path, collection)
            self.status["candidate_collection"] = {
                **collection,
                "path": rel(self.candidate_collection_path, self.repo_root),
            }
        except Exception as exc:
            self.status["candidate_collection"] = {
                "job_id": self.args.job_id,
                "registered": 0,
                "error": str(exc),
            }
        try:
            self.status["retention"] = {"removed_job_ids": self.prune_superseded_jobs()}
        except Exception as exc:
            self.status["retention"] = {"removed_job_ids": [], "error": str(exc)}
        write_json(self.status_path, self.status)

    def prune_superseded_jobs(self) -> List[str]:
        jobs_root = self.repo_root / "demo_runs" / "api_jobs"
        if not jobs_root.is_dir():
            return []

        protected_job_ids = {
            str(record.get("job_id", ""))
            for record in CandidateStore(self.repo_root).list()
            if record.get("job_id")
        }
        removed = []
        current_out = self.out.resolve()
        for status_path in sorted(jobs_root.glob("*/status.json")):
            job_dir = status_path.parent
            if job_dir.resolve() == current_out:
                continue
            try:
                status = json.loads(status_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if status.get("lib") != self.args.lib or status.get("api") != self.args.api:
                continue
            if status.get("status") not in {"success", "failed"}:
                continue
            job_id = str(status.get("job_id") or job_dir.name)
            if job_id in protected_job_ids:
                continue
            shutil.rmtree(job_dir)
            removed.append(job_id)
        return removed

    def mark_remaining_skipped(self, failed_stage: str) -> None:
        execution_stages = STAGE_ORDER[:-1]
        if failed_stage not in execution_stages:
            return
        start = execution_stages.index(failed_stage) + 1
        for stage in execution_stages[start:]:
            if self.status["stages"].get(stage) == "pending":
                self.status["stages"][stage] = "skipped"
        self.status["updated_at"] = now()
        write_json(self.status_path, self.status)

    def log_path(self, name: str) -> Path:
        self.logs.mkdir(parents=True, exist_ok=True)
        return self.logs / name

    def selected_gpu_sample(self) -> Optional[dict]:
        sample = collect_gpu_sample()
        try:
            selected_index = int(str(self.args.cuda_device).split(",", 1)[0])
        except ValueError:
            return None
        for gpu in sample.get("gpus", []):
            if gpu.get("index") == selected_index:
                return {
                    "collected_at": sample.get("collected_at"),
                    **gpu,
                }
        return None

    def record_metric(self, stage: str, started: float) -> None:
        metric = build_metric(
            stage=stage,
            elapsed_seconds=time.monotonic() - started,
            qwen_root=self.qwen_out,
            results_root=self.results_root,
            api=self.args.api,
            gpu_sample=self.selected_gpu_sample(),
        )
        append_metric(self.metrics_path, metric)

    def run_command(self, stage: str, cmd: List[str], log_name: str, env: Optional[dict] = None) -> int:
        log_path = self.log_path(log_name)
        self.status["logs"][stage] = rel(log_path, self.repo_root)
        self.update_stage(stage, "running")

        with log_path.open("w", encoding="utf-8") as log:
            log.write("$ " + " ".join(cmd) + "\n\n")
            log.flush()
            if self.args.dry_run:
                log.write("[dry-run] command not executed\n")
                return 0
            proc = subprocess.Popen(
                cmd,
                cwd=self.repo_root,
                stdout=log,
                stderr=subprocess.STDOUT,
                env=env,
                text=True,
            )
            started = time.monotonic()
            while proc.poll() is None:
                self.record_metric(stage, started)
                time.sleep(1)
            self.record_metric(stage, started)
            return int(proc.returncode)

    def check_prompt_library(self) -> Path:
        self.update_stage("prompt_check", "running")
        cdir = Path(self.args.constraints_dir)
        if not cdir.is_absolute():
            cdir = self.repo_root / cdir
        structured = cdir / self.args.api / "prompts" / "structured_info.txt"
        if not structured.is_file():
            raise FileNotFoundError(f"prompt library missing: {structured}")
        if not structured.read_text(encoding="utf-8", errors="replace").strip():
            raise ValueError(f"structured prompt is empty: {structured}")
        self.update_stage("prompt_check", "success")
        return structured

    def run_qwen_seed(self) -> int:
        cmd = [
            sys.executable,
            "qwen_seed.py",
            "--library",
            self.args.lib,
            "--api",
            self.args.api,
            "--out_dir",
            rel(self.qwen_out, self.repo_root),
            "--constraints_dir",
            self.args.constraints_dir,
            "--model_path",
            self.args.qwen_model,
            "--dtype",
            self.args.dtype,
            "--ablation",
            "full",
            "--n_samples",
            str(self.args.qwen_n_samples),
            "--min_valid",
            str(self.args.qwen_min_valid),
            "--max_rounds",
            str(self.args.qwen_max_rounds),
            "--per_api_budget",
            str(self.args.qwen_per_api_budget),
            "--validate_timeout",
            str(self.args.qwen_validate_timeout),
        ]
        if self.args.force_redo:
            cmd.append("--force_redo")
        return self.run_command("qwen_seed", cmd, "01_qwen_seed.log")

    def run_ev_generation(self) -> int:
        env = os.environ.copy()
        env["CUDA_VISIBLE_DEVICES"] = str(self.args.cuda_device)
        cmd = [
            sys.executable,
            "ev_generation.py",
            "--model_name",
            self.args.mut_model,
            "--library",
            self.args.lib,
            "--api",
            self.args.api,
            "--seedfolder",
            rel(self.qwen_out / "fix", self.repo_root),
            "--folder",
            rel(self.results_root, self.repo_root),
            "--max_valid",
            str(self.args.ev_max_valid),
            "--timeout",
            str(self.args.ev_timeout),
            "--batch_size",
            str(self.args.ev_batch_size),
            "--random_seed",
            str(self.args.random_seed),
            "--only_valid",
            "--seed_selection_algo",
            "fitness",
            "--mutator_selection_algo",
            "ts",
            "--seed_pool_size",
            str(self.args.seed_pool_size),
            "--relaxargmut",
        ]
        return self.run_command("ev_generation", cmd, "02_ev_generation.log", env=env)

    def run_driver(self) -> int:
        cmd = [
            sys.executable,
            "driver.py",
            "--mode",
            "race",
            "--input",
            rel(self.results_root, self.repo_root),
            "--output",
            rel(self.results_root / "trace.txt", self.repo_root),
        ]
        if self.args.lib == "tf":
            cmd.append("--tf")
        return self.run_command("driver", cmd, "03_driver.log")

    def belongs_to_api(self, path: Path) -> bool:
        if path.suffix != ".py":
            return False
        return path.stem.rsplit("_", 1)[0] == self.args.api

    def publish_results_to_canonical(self) -> None:
        for name in RESULT_SUBDIRS:
            src_dir = self.results_root / name
            dst_dir = self.canonical_results_root / name
            dst_dir.mkdir(parents=True, exist_ok=True)

            for old_file in dst_dir.glob("*.py"):
                if self.belongs_to_api(old_file):
                    old_file.unlink()

            if not src_dir.is_dir():
                continue
            for src_file in sorted(src_dir.glob("*.py")):
                if self.belongs_to_api(src_file):
                    shutil.copy2(src_file, dst_dir / src_file.name)

        trace_path = self.results_root / "trace.txt"
        if trace_path.is_file():
            trace_dir = self.canonical_results_root / "single_api_traces"
            trace_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(trace_path, trace_dir / f"{safe_name(self.args.api)}.txt")

    def collect_counts(self) -> dict:
        qwen_fix_dir = self.qwen_out / "fix" / self.args.api
        result_counts = {
            name: count_py(self.results_root / name)
            for name in RESULT_SUBDIRS
        }
        trace_path = self.results_root / "trace.txt"
        return {
            "qwen_valid_seed_count": count_py(qwen_fix_dir),
            "result_counts": result_counts,
            "trace_path": rel(trace_path, self.repo_root),
            "trace_exists": trace_path.is_file(),
            "catch_count": count_trace_hits(trace_path),
        }

    def write_summary(self, status: str, error: Optional[str] = None) -> dict:
        counts = self.collect_counts()
        summary = {
            "job_id": self.args.job_id,
            "lib": self.args.lib,
            "api": self.args.api,
            "mode": self.args.mode,
            "dry_run": self.args.dry_run,
            "prompt_library": "found",
            "qwen_model": self.args.qwen_model,
            "mutation_model": self.args.mut_model,
            "status": status,
            "error": error,
            "canonical_results_path": rel(self.canonical_results_root, self.repo_root),
            **counts,
            "logs": self.status.get("logs", {}),
            "updated_at": now(),
        }
        write_json(self.summary_json_path, summary)
        self.summary_md_path.write_text(self.summary_markdown(summary), encoding="utf-8")
        self.update_stage("summary", "success" if status != "failed" else "failed", error=error)
        return summary

    def summary_markdown(self, summary: dict) -> str:
        result_counts = summary["result_counts"]
        lines = [
            f"# Single API Demo Report: `{summary['api']}`",
            "",
            f"- Library: `{summary['lib']}`",
            f"- Status: `{summary['status']}`",
            f"- Dry run: `{summary['dry_run']}`",
            f"- Qwen model: `{summary['qwen_model']}`",
            f"- Mutation model: `{summary['mutation_model']}`",
            f"- Valid Qwen seeds: `{summary['qwen_valid_seed_count']}`",
            f"- Trace: `{summary['trace_path']}`",
            f"- Trace hit lines: `{summary['catch_count']}`",
            "",
            "## Result Counts",
            "",
        ]
        for name in ("seed", "valid", "exception", "crash", "notarget", "hangs", "flaky"):
            lines.append(f"- {name}: `{result_counts.get(name, 0)}`")
        if summary.get("error"):
            lines.extend(["", "## Error", "", summary["error"]])
        lines.extend(["", "## Log Tails", ""])
        for stage, log_rel in summary.get("logs", {}).items():
            lines.append(f"### {stage}")
            lines.append("")
            tail = read_tail(self.repo_root / log_rel, max_chars=1200)
            lines.append("```text")
            lines.append(tail.rstrip())
            lines.append("```")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def run(self) -> int:
        if self.out.exists() and self.args.force_redo:
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.logs.mkdir(parents=True, exist_ok=True)
        write_json(self.environment_path, collect_environment())
        write_json(self.status_path, self.status)

        try:
            self.check_prompt_library()
        except Exception as exc:
            message = str(exc)
            self.update_stage("prompt_check", "failed", error=message)
            self.mark_remaining_skipped("prompt_check")
            self.write_summary("failed", error=message)
            self.finish("failed", error=message)
            print(message)
            return 1

        if self.run_qwen_seed() != 0:
            error = "qwen_seed.py failed; see logs/01_qwen_seed.log"
            self.update_stage("qwen_seed", "failed", error=error)
            self.mark_remaining_skipped("qwen_seed")
            self.write_summary("failed", error=error)
            self.finish("failed", error=error)
            return 1
        self.update_stage("qwen_seed", "success")

        qwen_valid = count_py(self.qwen_out / "fix" / self.args.api)
        if qwen_valid == 0 and not self.args.dry_run:
            error = "Qwen produced zero valid fixed seeds; stop before mutation"
            self.mark_remaining_skipped("qwen_seed")
            self.write_summary("failed", error=error)
            self.finish("failed", error=error)
            print(error)
            return 1

        if self.run_ev_generation() != 0:
            error = "ev_generation.py failed; see logs/02_ev_generation.log"
            self.update_stage("ev_generation", "failed", error=error)
            self.mark_remaining_skipped("ev_generation")
            self.write_summary("failed", error=error)
            self.finish("failed", error=error)
            return 1
        self.update_stage("ev_generation", "success")

        if self.run_driver() != 0:
            error = "driver.py failed; see logs/03_driver.log"
            self.update_stage("driver", "failed", error=error)
            self.write_summary("failed", error=error)
            self.finish("failed", error=error)
            return 1
        self.update_stage("driver", "success")

        if not self.args.dry_run:
            self.publish_results_to_canonical()

        self.write_summary("success")
        self.finish("success")
        print(f"summary: {self.summary_md_path}")
        return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one API through TensorGuard demo pipeline.")
    parser.add_argument("--lib", required=True, choices=["torch", "tf"])
    parser.add_argument("--api", required=True)
    parser.add_argument("--constraints_dir", default=None)
    parser.add_argument("--qwen_model", default="../Qwen2.5-Coder-7B-Instruct")
    parser.add_argument("--dtype", default="bfloat16", choices=["bfloat16", "float16", "float32"])
    parser.add_argument("--mut_model", default="facebook/incoder-1B")
    parser.add_argument("--out", default=None)
    parser.add_argument("--mode", default="demo", choices=["demo", "normal"])
    parser.add_argument("--cuda_device", default="0")
    parser.add_argument("--random_seed", type=int, default=420)
    parser.add_argument("--seed_pool_size", type=int, default=10)
    parser.add_argument("--job_id", default=None)
    parser.add_argument("--force_redo", action="store_true")
    parser.add_argument("--dry_run", action="store_true")

    defaults = mode_defaults("normal")
    parser.add_argument("--qwen_n_samples", type=int, default=None)
    parser.add_argument("--qwen_min_valid", type=int, default=None)
    parser.add_argument("--qwen_max_rounds", type=int, default=None)
    parser.add_argument("--qwen_per_api_budget", type=float, default=None)
    parser.add_argument("--qwen_validate_timeout", type=int, default=None)
    parser.add_argument("--ev_max_valid", type=int, default=None)
    parser.add_argument("--ev_batch_size", type=int, default=None)
    parser.add_argument("--ev_timeout", type=int, default=None)

    args = parser.parse_args()
    mode_cfg = mode_defaults(args.mode)
    for key in defaults:
        if getattr(args, key) is None:
            setattr(args, key, mode_cfg[key])
    if args.constraints_dir is None:
        args.constraints_dir = f"experiment/{args.lib}"
    if args.out is None:
        args.out = f"demo_runs/{safe_name(args.api)}_{args.mode}"
    if args.job_id is None:
        args.job_id = f"{safe_name(args.api)}_{_dt.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    return args


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    args = parse_args()
    return DemoRun(args, repo_root).run()


if __name__ == "__main__":
    raise SystemExit(main())
