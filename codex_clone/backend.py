"""Backend helper: download model and start a local server.

This tries to use ``llama_cpp.server`` if it is installed.
If the module is missing, the script will still download the
model and then print clear instructions instead of crashing.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Final

from huggingface_hub import hf_hub_download


HF_REPO: Final[str] = "TheBloke/deepseek-coder-6.7B-instruct-GGUF"
HF_FILE: Final[str] = "deepseek-coder-6.7b-instruct.Q4_K_M.gguf"
DEFAULT_PORT: Final[int] = 1234


try:  # pragma: no cover - presence of backend is environment-specific
    import llama_cpp.server as _llama_server  # type: ignore[unused-ignore]
    HAVE_LLAMA_CPP = True
except Exception:  # pragma: no cover - import error path
    HAVE_LLAMA_CPP = False


def _project_root() -> Path:
    """Return the project root folder."""
    here = Path(__file__).resolve()
    return here.parent.parent


def _models_dir() -> Path:
    """Return the local models directory."""
    root = _project_root()
    directory = root / "models"
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def local_model_path() -> Path:
    """Return the expected local model path."""
    return _models_dir() / HF_FILE


def download_model() -> Path:
    """Ensure the GGUF model exists locally and return its path."""
    path = local_model_path()
    if path.exists():
        return path
    local_path = hf_hub_download(
        repo_id=HF_REPO,
        filename=HF_FILE,
        local_dir=str(path.parent),
        local_dir_use_symlinks=False,
    )
    return Path(local_path)


def _print_no_llama_message(model_path: Path) -> None:
    """Explain what to do if llama-cpp is not available."""
    lines = [
        "llama-cpp-python is not installed; cannot start built-in backend.",
        "",
        "The model has been downloaded to:",
        f"  {model_path}",
        "",
        "You now have two main options:",
        "  1) Install llama-cpp-python with a C++ toolchain and retry, or",
        "  2) Use another local server (LM Studio, llama.cpp binary, etc.)",
        "     pointing at the GGUF path above.",
        "",
        "Example llama.cpp command (if you have `llama-server`):",
        "  llama-server --model "{model_path}" --host 127.0.0.1 --port 1234 \",
        "      --alias local-coder --ctx-size 8192",
        "",
        "Then run:  python -m codex_clone.repl",
    ]
    print("\n".join(lines), file=sys.stderr)


def run_server(port: int = DEFAULT_PORT) -> None:
    """Download the model if needed and start llama-cpp server."""
    model_path = download_model()
    if not HAVE_LLAMA_CPP:
        _print_no_llama_message(model_path)
        sys.exit(1)
    cmd = [
        sys.executable,
        "-m",
        "llama_cpp.server",
        "--model",
        str(model_path),
        "--model_alias",
        "local-coder",
        "--host",
        "127.0.0.1",
        "--port",
        str(port),
        "--n_ctx",
        "8192",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    run_server()
