
@echo off
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

if not exist ".venv" (
    python -m venv .venv
)

call ".venv\Scripts\activate.bat"

pip install -e . >nul
pip install "llama-cpp-python[server]" huggingface_hub >nul

python -m codex_clone.backend %*
