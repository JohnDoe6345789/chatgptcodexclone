# Local Codex Clone (CLI)

Tiny terminal chat client that talks to any OpenAI-compatible
HTTP endpoint running on your own machine (LM Studio, llamafile,
Ollama-with-proxy, etc.).

It is focused on code: you get a ChatGPT/Codex-style loop in
your shell, but the actual model is whatever you run locally.

## Quick start

1. Start a local server that exposes the
   `/v1/chat/completions` endpoint, for example LM Studio.

   Make sure it is listening on `http://localhost:1234` or set
   `CODEX_BASE_URL` to match.

2. Install the package in editable mode:

   ```bash
   cd codex_clone
   python -m venv .venv
   . .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   pip install -e .
   ```

3. Run the REPL:

   ```bash
   python -m codex_clone.repl
   ```

Type your prompt, press Enter. You can keep typing multiple
lines; an empty line sends the block. Type `exit` or `quit` to
leave.

## Configuration

Environment variables:

- `CODEX_BASE_URL` (default: `http://localhost:1234`)
- `CODEX_API_KEY` (optional, usually empty for local)
- `CODEX_MODEL` (default: `local-coder`)
- `CODEX_SYSTEM_PROMPT` (default: short coding prompt)
- `CODEX_TEMPERATURE` (default: `0.2`)
- `CODEX_MAX_TOKENS` (default: `2048`)

## Running tests

```bash
python -m unittest discover -s tests
```
