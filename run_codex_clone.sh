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

python -m codex_clone.repl "$@"
