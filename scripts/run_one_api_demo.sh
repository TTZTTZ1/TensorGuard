#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ ! -f "${REPO_ROOT}/qwen_seed.py" || ! -f "${REPO_ROOT}/ev_generation.py" || ! -f "${REPO_ROOT}/driver.py" ]]; then
  echo "error: this script must live under a TensorGuard checkout" >&2
  exit 1
fi

cd "${REPO_ROOT}"
python3 scripts/run_one_api_demo.py "$@"
