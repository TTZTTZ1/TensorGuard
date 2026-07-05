#!/usr/bin/env python3
"""Run all APIs through the TensorGuard pipeline.

This script reads an API list file and runs the full pipeline for each API:
  prompt library check -> qwen_seed.py -> ev_generation.py -> driver.py

Usage:
  # Run all PyTorch APIs
  python scripts/run_all_apis.py --lib torch

  # Run all TensorFlow APIs
  python scripts/run_all_apis.py --lib tf

  # Run with custom settings
  python scripts/run_all_apis.py --lib torch --mode full --max_workers 2
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import List, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def now() -> str:
    return _dt.datetime.now().isoformat(timespec="seconds")


def read_api_list(path: Path) -> List[str]:
    """Read API list from file, one API per line."""
    if not path.is_file():
        raise FileNotFoundError(f"API list not found: {path}")
    apis = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            api = line.strip()
            if api and not api.startswith("#"):
                apis.append(api)
    return apis


def run_single_api(
    lib: str,
    api: str,
    out_dir: Path,
    mode: str,
    dry_run: bool,
    qwen_model: str,
    mut_model: str,
    cuda_device: int,
) -> dict:
    """Run a single API through the pipeline."""
    api_safe = api.replace(".", "_").replace("/", "_")
    job_out = out_dir / api_safe

    cmd = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "run_one_api_demo.py"),
        "--lib", lib,
        "--api", api,
        "--out", str(job_out),
        "--mode", mode,
        "--qwen_model", qwen_model,
        "--mut_model", mut_model,
        "--cuda_device", str(cuda_device),
    ]

    if dry_run:
        cmd.append("--dry_run")

    start_time = time.time()
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=3600,  # 1 hour timeout per API
        )
        elapsed = time.time() - start_time
        return {
            "api": api,
            "status": "success" if result.returncode == 0 else "failed",
            "returncode": result.returncode,
            "elapsed": round(elapsed, 2),
            "stdout": result.stdout[-2000:] if result.stdout else "",
            "stderr": result.stderr[-2000:] if result.stderr else "",
            "job_dir": str(job_out),
        }
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        return {
            "api": api,
            "status": "timeout",
            "returncode": -1,
            "elapsed": round(elapsed, 2),
            "stdout": "",
            "stderr": "Timeout after 3600 seconds",
            "job_dir": str(job_out),
        }
    except Exception as e:
        elapsed = time.time() - start_time
        return {
            "api": api,
            "status": "error",
            "returncode": -1,
            "elapsed": round(elapsed, 2),
            "stdout": "",
            "stderr": str(e),
            "job_dir": str(job_out),
        }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run all APIs through the TensorGuard pipeline."
    )
    parser.add_argument(
        "--lib",
        required=True,
        choices=["torch", "tf"],
        help="Target library (torch or tf).",
    )
    parser.add_argument(
        "--apilist",
        default=None,
        help="Path to API list file. Defaults to data/<lib>_apis.txt.",
    )
    parser.add_argument(
        "--out_dir",
        default=None,
        help="Output directory. Defaults to batch_runs/<lib>_<timestamp>.",
    )
    parser.add_argument(
        "--mode",
        default="full",
        choices=["demo", "full"],
        help="Run mode (demo=fast, full=complete). Default: full.",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Dry run mode (no model loading).",
    )
    parser.add_argument(
        "--max_workers",
        type=int,
        default=1,
        help="Max parallel workers. Default: 1.",
    )
    parser.add_argument(
        "--qwen_model",
        default="../Qwen2.5-Coder-7B-Instruct",
        help="Qwen model path.",
    )
    parser.add_argument(
        "--mut_model",
        default="facebook/incoder-6B",
        help="Mutation model path.",
    )
    parser.add_argument(
        "--cuda_device",
        type=int,
        default=0,
        help="CUDA device ID.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip APIs that already have results.",
    )
    args = parser.parse_args()

    # Resolve paths
    repo_root = REPO_ROOT
    if args.apilist:
        apilist_path = Path(args.apilist)
        if not apilist_path.is_absolute():
            apilist_path = repo_root / apilist_path
    else:
        apilist_path = repo_root / "data" / f"{args.lib}_apis.txt"

    # Read API list
    apis = read_api_list(apilist_path)
    print(f"[{now()}] Loaded {len(apis)} APIs from {apilist_path}")

    # Setup output directory
    if args.out_dir:
        out_dir = Path(args.out_dir)
        if not out_dir.is_absolute():
            out_dir = repo_root / out_dir
    else:
        timestamp = _dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        out_dir = repo_root / "batch_runs" / f"{args.lib}_{timestamp}"

    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[{now()}] Output directory: {out_dir}")

    # Save run config
    config = {
        "lib": args.lib,
        "apilist": str(apilist_path),
        "mode": args.mode,
        "dry_run": args.dry_run,
        "max_workers": args.max_workers,
        "qwen_model": args.qwen_model,
        "mut_model": args.mut_model,
        "cuda_device": args.cuda_device,
        "total_apis": len(apis),
        "started_at": now(),
    }
    config_path = out_dir / "batch_config.json"
    config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    # Filter APIs if resuming
    if args.resume:
        remaining_apis = []
        for api in apis:
            api_safe = api.replace(".", "_").replace("/", "_")
            job_dir = out_dir / api_safe
            status_path = job_dir / "status.json"
            if status_path.is_file():
                try:
                    status = json.loads(status_path.read_text(encoding="utf-8"))
                    if status.get("status") == "success":
                        continue
                except (OSError, json.JSONDecodeError):
                    pass
            remaining_apis.append(api)
        print(f"[{now()}] Resuming: {len(remaining_apis)}/{len(apis)} APIs remaining")
        apis = remaining_apis

    # Run APIs
    results = []
    start_time = time.time()

    if args.max_workers <= 1:
        # Sequential execution
        for i, api in enumerate(apis, 1):
            print(f"\n[{now()}] [{i}/{len(apis)}] Running {api}...")
            result = run_single_api(
                lib=args.lib,
                api=api,
                out_dir=out_dir,
                mode=args.mode,
                dry_run=args.dry_run,
                qwen_model=args.qwen_model,
                mut_model=args.mut_model,
                cuda_device=args.cuda_device,
            )
            results.append(result)
            status_icon = "✓" if result["status"] == "success" else "✗"
            print(f"[{now()}] [{i}/{len(apis)}] {status_icon} {api}: {result['status']} ({result['elapsed']}s)")
    else:
        # Parallel execution
        print(f"[{now()}] Running with {args.max_workers} workers...")
        with ProcessPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {
                executor.submit(
                    run_single_api,
                    lib=args.lib,
                    api=api,
                    out_dir=out_dir,
                    mode=args.mode,
                    dry_run=args.dry_run,
                    qwen_model=args.qwen_model,
                    mut_model=args.mut_model,
                    cuda_device=args.cuda_device,
                ): api
                for api in apis
            }

            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                results.append(result)
                status_icon = "✓" if result["status"] == "success" else "✗"
                print(f"[{now()}] [{i}/{len(apis)}] {status_icon} {result['api']}: {result['status']} ({result['elapsed']}s)")

    # Save results
    total_elapsed = time.time() - start_time
    summary = {
        "config": config,
        "completed_at": now(),
        "total_elapsed": round(total_elapsed, 2),
        "total_apis": len(apis),
        "success": sum(1 for r in results if r["status"] == "success"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "timeout": sum(1 for r in results if r["status"] == "timeout"),
        "error": sum(1 for r in results if r["status"] == "error"),
        "results": sorted(results, key=lambda x: x["api"]),
    }

    summary_path = out_dir / "batch_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    # Print summary
    print(f"\n{'='*60}")
    print(f"[{now()}] Batch run completed")
    print(f"  Total APIs: {summary['total_apis']}")
    print(f"  Success:    {summary['success']}")
    print(f"  Failed:     {summary['failed']}")
    print(f"  Timeout:    {summary['timeout']}")
    print(f"  Error:      {summary['error']}")
    print(f"  Elapsed:    {round(total_elapsed / 60, 1)} minutes")
    print(f"  Summary:    {summary_path}")
    print(f"{'='*60}")

    return 0 if summary["failed"] == 0 and summary["error"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
