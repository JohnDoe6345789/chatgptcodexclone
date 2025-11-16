#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${script_dir}"

if [ ! -d .venv ]; then
    python -m venv .venv
fi

# shellcheck disable=SC1091
. .venv/bin/activate

pip install -e . >/dev/null

if ! python -m pip show llama-cpp-python >/dev/null 2>&1; then
    echo "[info] llama-cpp-python not found, attempting install..."
    if ! python -m pip install "llama-cpp-python[server]"; then
        echo "[warn] Failed to install llama-cpp-python[server]."
        echo "[warn] You can still use the downloaded model with"
        echo "[warn] an external server (LM Studio, llama.cpp binary, etc.)."
    fi
fi

python -m codex_clone.backend "$@"
