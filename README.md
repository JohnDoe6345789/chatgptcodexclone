# Local Codex Clone (CLI + backend)

Tiny terminal chat client plus a helper backend launcher that
runs DeepSeek Coder 6.7B Instruct (GGUF) locally via llama-cpp.

You get a ChatGPT/Codex-style loop in your shell, but the model
and all requests stay on your own machine.

## What you get

- `python -m codex_clone.backend`
  - Downloads a quantised DeepSeek Coder 6.7B Instruct GGUF
    from Hugging Face (Q4_K_M via TheBloke).
  - Starts `llama_cpp.server` on `http://127.0.0.1:1234/v1`
    with model alias `local-coder`.
- `python -m codex_clone.repl`
  - Simple chat REPL that talks to that server using an
    OpenAI-compatible JSON API.

## Quick start

1. Create a virtualenv and install:

   ```bash
   cd codex_clone_v2
   python -m venv .venv
   . .venv/bin/activate        # On Windows: .venv\\Scripts\\activate
   pip install -e .
   ```

2. Install runtime deps for the backend:

   ```bash
   pip install "llama-cpp-python[server]" huggingface_hub
   ```

3. Start the backend in one terminal:

   ```bash
   python -m codex_clone.backend
   ```

   First run will download one GGUF file into `./models`.
   After that it just starts the server.

4. In another terminal, run the REPL:

   ```bash
   python -m codex_clone.repl
   ```

   Type your coding questions, press Enter. Use an empty line
   to send the current block. Type `exit` or `quit` to leave.

## Scripts

For convenience there are helper scripts that do the above:

- `run_backend.sh` / `run_backend.bat`
  - Create `.venv` if needed.
  - Install required packages.
  - Start the llama-cpp backend.

- `run_codex_clone.sh` / `run_codex_clone.bat`
  - Re-use `.venv` and drop you into the REPL.

## Configuration

The REPL reads these environment variables:

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
