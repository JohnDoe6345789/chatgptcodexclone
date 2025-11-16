
@echo off
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

if not exist ".venv" (
    python -m venv .venv
)

call ".venv\Scripts\activate.bat"

pip install -e . >nul

python -m codex_clone.repl %*
