"""Backend helper: download model and start llama-cpp server."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Final

from huggingface_hub import hf_hub_download


HF_REPO: Final[str] = "TheBloke/deepseek-coder-6.7B-instruct-GGUF"
HF_FILE: Final[str] = "deepseek-coder-6.7b-instruct.Q4_K_M.gguf"
DEFAULT_PORT: Final[int] = 1234


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


def _local_model_path() -> Path:
    """Return the expected local model path."""
    return _models_dir() / HF_FILE


def download_model() -> Path:
    """Ensure the GGUF model exists locally and return its path."""
    path = _local_model_path()
    if path.exists():
        return path
    local_path = hf_hub_download(
        repo_id=HF_REPO,
        filename=HF_FILE,
        local_dir=str(path.parent),
        local_dir_use_symlinks=False,
    )
    return Path(local_path)


def run_server(port: int = DEFAULT_PORT) -> None:
    """Download the model if needed and start llama-cpp server."""
    model_path = download_model()
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
