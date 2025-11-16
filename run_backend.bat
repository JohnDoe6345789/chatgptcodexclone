
@echo off
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

if not exist ".venv" (
    python -m venv .venv
)

call ".venv\Scripts\activate.bat"

pip install -e . >nul

python -m pip show llama-cpp-python >nul 2>nul
if errorlevel 1 (
    echo [info] llama-cpp-python not found, attempting install...
    python -m pip install "llama-cpp-python[server]"
    if errorlevel 1 (
        echo [warn] Failed to install llama-cpp-python[server].
        echo [warn] You can still use the downloaded model with an external server.
    )
)

python -m codex_clone.backend %*
