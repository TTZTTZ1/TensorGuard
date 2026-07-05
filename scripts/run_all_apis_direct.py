#!/usr/bin/env python3
"""Run all APIs through the TensorGuard pipeline (direct version).

This script directly orchestrates the full pipeline for each API:
  1. prompt library check
  2. qwen_seed.py (seed generation)
  3. ev_generation.py (evolutionary mutation)
  4. driver.py (CPU/GPU differential detection)

Usage:
  # Run all PyTorch APIs
  python scripts/run_all_apis_direct.py --lib torch

  # Run all TensorFlow APIs
  python scripts/run_all_apis_direct.py --lib tf

  # Run with custom settings
  python scripts/run_all_apis_direct.py --lib torch --max_workers 2
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


def run_command(cmd: List[str], cwd: Path, timeout: int = 3600) -> dict:
    """Run a command and return result."""
    start_time = time.time()
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        elapsed = time.time() - start_time
        return {
            "returncode": result.returncode,
            "elapsed": round(elapsed, 2),
            "stdout": result.stdout[-2000:] if result.stdout else "",
            "stderr": result.stderr[-2000:] if result.stderr else "",
        }
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        return {
            "returncode": -1,
            "elapsed": round(elapsed, 2),
            "stdout": "",
            "stderr": f"Timeout after {timeout} seconds",
        }
    except Exception as e:
        elapsed = time.time() - start_time
        return {
            "returncode": -1,
            "elapsed": round(elapsed, 2),
            "stdout": "",
            "stderr": str(e),
        }


def check_prompt_library(lib: str, api: str, constraints_dir: Path) -> dict:
    """Check if prompt library exists for the API."""
    structured = constraints_dir / api / "prompts" / "structured_info.txt"
    if not structured.is_file():
        return {"status": "failed", "error": f"prompt library missing: {structured}"}
    if not structured.read_text(encoding="utf-8", errors="replace").strip():
        return {"status": "failed", "error": f"structured prompt is empty: {structured}"}
    return {"status": "success"}


def run_qwen_seed(
    lib: str,
    api: str,
    out_dir: Path,
    constraints_dir: Path,
    model_path: str,
    dtype: str,
    n_samples: int,
    min_valid: int,
    max_rounds: int,
    per_api_budget: float,
    validate_timeout: int,
    dry_run: bool,
) -> dict:
    """Run qwen_seed.py for seed generation."""
    cmd = [
        sys.executable,
        str(REPO_ROOT / "qwen_seed.py"),
        "--library", lib,
        "--api", api,
        "--out_dir", str(out_dir),
        "--constraints_dir", str(constraints_dir),
        "--model_path", model_path,
        "--dtype", dtype,
        "--ablation", "full",
        "--n_samples", str(n_samples),
        "--min_valid", str(min_valid),
        "--max_rounds", str(max_rounds),
        "--per_api_budget", str(per_api_budget),
        "--validate_timeout", str(validate_timeout),
    ]
    if dry_run:
        cmd.append("--force_redo")
    return run_command(cmd, REPO_ROOT, timeout=per_api_budget + 60)


def run_ev_generation(
    lib: str,
    api: str,
    seedfolder: Path,
    results_folder: Path,
    model_name: str,
    max_valid: int,
    timeout: int,
    batch_size: int,
    random_seed: int,
    seed_pool_size: int,
    cuda_device: int,
    dry_run: bool,
) -> dict:
    """Run ev_generation.py for evolutionary mutation."""
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(cuda_device)

    cmd = [
        sys.executable,
        str(REPO_ROOT / "ev_generation.py"),
        "--model_name", model_name,
        "--library", lib,
        "--api", api,
        "--seedfolder", str(seedfolder),
        "--folder", str(results_folder),
        "--max_valid", str(max_valid),
        "--timeout", str(timeout),
        "--batch_size", str(batch_size),
        "--random_seed", str(random_seed),
        "--only_valid",
        "--seed_selection_algo", "fitness",
        "--mutator_selection_algo", "ts",
        "--seed_pool_size", str(seed_pool_size),
        "--relaxargmut",
    ]
    if dry_run:
        cmd.append("--only_valid")
    return run_command(cmd, REPO_ROOT, timeout=timeout + 60)


def run_driver(
    lib: str,
    results_folder: Path,
    dry_run: bool,
) -> dict:
    """Run driver.py for CPU/GPU differential detection."""
    cmd = [
        sys.executable,
        str(REPO_ROOT / "driver.py"),
        "--mode", "race",
        "--input", str(results_folder),
        "--output", str(results_folder / "trace.txt"),
    ]
    if lib == "tf":
        cmd.append("--tf")
    if dry_run:
        cmd.append("--dry_run")
    return run_command(cmd, REPO_ROOT, timeout=600)


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
    """Run a single API through the full pipeline."""
    api_safe = api.replace(".", "_").replace("/", "_")
    job_out = out_dir / api_safe
    job_out.mkdir(parents=True, exist_ok=True)

    # Setup paths
    constraints_dir = REPO_ROOT / "experiment" / lib
    qwen_out = job_out / "qwen_seed"
    results_folder = job_out / "Results" / lib

    # Mode settings
    if mode == "demo":
        qwen_params = {
            "n_samples": 5,
            "min_valid": 2,
            "max_rounds": 1,
            "per_api_budget": 300,
            "validate_timeout": 30,
        }
        ev_params = {
            "max_valid": 5,
            "batch_size": 1,
            "timeout": 300,
        }
    else:  # full
        qwen_params = {
            "n_samples": 10,
            "min_valid": 5,
            "max_rounds": 2,
            "per_api_budget": 600,
            "validate_timeout": 30,
        }
        ev_params = {
            "max_valid": 200,
            "batch_size": 100,
            "timeout": 1000,
        }

    start_time = time.time()
    stages = {}

    # Stage 1: Check prompt library
    print(f"  [{now()}] [{api}] Stage 1: Checking prompt library...")
    result = check_prompt_library(lib, api, constraints_dir)
    stages["prompt_check"] = result
    if result["status"] != "success":
        return {
            "api": api,
            "status": "failed",
            "stage": "prompt_check",
            "elapsed": round(time.time() - start_time, 2),
            "stages": stages,
            "job_dir": str(job_out),
        }

    # Stage 2: Run qwen_seed
    print(f"  [{now()}] [{api}] Stage 2: Running qwen_seed...")
    result = run_qwen_seed(
        lib=lib,
        api=api,
        out_dir=qwen_out,
        constraints_dir=constraints_dir,
        model_path=qwen_model,
        dtype="bfloat16",
        dry_run=dry_run,
        **qwen_params,
    )
    stages["qwen_seed"] = result
    if result["returncode"] != 0:
        return {
            "api": api,
            "status": "failed",
            "stage": "qwen_seed",
            "elapsed": round(time.time() - start_time, 2),
            "stages": stages,
            "job_dir": str(job_out),
        }

    # Stage 3: Run ev_generation
    print(f"  [{now()}] [{api}] Stage 3: Running ev_generation...")
    result = run_ev_generation(
        lib=lib,
        api=api,
        seedfolder=qwen_out / "fix",
        results_folder=results_folder,
        model_name=mut_model,
        cuda_device=cuda_device,
        dry_run=dry_run,
        **ev_params,
    )
    stages["ev_generation"] = result
    if result["returncode"] != 0:
        return {
            "api": api,
            "status": "failed",
            "stage": "ev_generation",
            "elapsed": round(time.time() - start_time, 2),
            "stages": stages,
            "job_dir": str(job_out),
        }

    # Stage 4: Run driver
    print(f"  [{now()}] [{api}] Stage 4: Running driver...")
    result = run_driver(
        lib=lib,
        results_folder=results_folder,
        dry_run=dry_run,
    )
    stages["driver"] = result
    if result["returncode"] != 0:
        return {
            "api": api,
            "status": "failed",
            "stage": "driver",
            "elapsed": round(time.time() - start_time, 2),
            "stages": stages,
            "job_dir": str(job_out),
        }

    elapsed = time.time() - start_time
    return {
        "api": api,
        "status": "success",
        "elapsed": round(elapsed, 2),
        "stages": stages,
        "job_dir": str(job_out),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run all APIs through the TensorGuard pipeline (direct version)."
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
