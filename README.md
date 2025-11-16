# Local Codex Clone (smart backend)

This version adds safer, "smart" backend handling:

- Downloads DeepSeek Coder 6.7B Instruct (GGUF) via `huggingface_hub`.
- *Tries* to start `llama_cpp.server` **if available**.
- If `llama-cpp-python` is missing or fails to build, it:
  - Still downloads the model,
  - Prints the exact GGUF path,
  - Explains how to run an external server instead,
  - Exits cleanly instead of crashing with a traceback.

The chat REPL is unchanged: it just talks to any
OpenAI-compatible endpoint (LM Studio, llama.cpp, etc.).

## Quick start (basic)

1. Create a virtualenv and install:

   ```bash
   cd codex_clone_smart
   python -m venv .venv
   . .venv/bin/activate        # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

2. Install an OpenAI-compatible backend by **one** of these options:

   - (A) `llama-cpp-python[server]` with a C++ toolchain (harder on Windows),
   - (B) LM Studio / other GUI that exposes `/v1/chat/completions`,
   - (C) Prebuilt `llama-server` binary from llama.cpp.

3. To let the helper try to start `llama_cpp.server` and at least
   download the model, run:

   ```bash
   python -m codex_clone.backend
   ```

   - If `llama-cpp-python` is installed and working, this will
     start `llama_cpp.server` on `127.0.0.1:1234` with alias
     `local-coder`.
   - If not, you will get a short message describing what to do
     and where the GGUF model lives.

4. In another terminal, run the REPL:

   ```bash
   python -m codex_clone.repl
   ```

   The REPL talks to `http://localhost:1234/v1/chat/completions`
   by default, but you can point it anywhere via env vars.

## Helper scripts

- `run_backend.sh` / `run_backend.bat`

  - Create `.venv` if needed.
  - Install this package.
  - *Attempt* to install `llama-cpp-python[server]`, but do not
    treat failure as fatal.
  - Run `python -m codex_clone.backend`.

- `run_codex_clone.sh` / `run_codex_clone.bat`

  - Re-use `.venv` and drop you into the REPL.

## Environment variables (REPL)

- `CODEX_BASE_URL` (default: `http://localhost:1234`)
- `CODEX_API_KEY` (not used for local server)
- `CODEX_MODEL` (default: `local-coder`)
- `CODEX_SYSTEM_PROMPT`
- `CODEX_TEMPERATURE` (default: `0.2`)
- `CODEX_MAX_TOKENS` (default: `2048`)

## Tests

```bash
python -m unittest discover -s tests
```
