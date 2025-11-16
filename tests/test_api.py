"""Tests for the API helper functions."""

from __future__ import annotations

import json
import unittest

from codex_clone.config import Config
from codex_clone.api import (
    _build_payload,
    _parse_response,
    CodexError,
)


class ApiTests(unittest.TestCase):
    """Small unit tests for payload and parsing."""

    def _dummy_config(self) -> Config:
        return Config(
            base_url="http://localhost:1234",
            api_key=None,
            model="dummy-model",
            system_prompt="x",
            temperature=0.0,
            max_tokens=16,
        )

    def test_build_payload_contains_messages(self) -> None:
        config = self._dummy_config()
        messages = [{"role": "user", "content": "hi"}]
        data = _build_payload(messages, config)
        obj = json.loads(data.decode("utf-8"))
        self.assertEqual(obj["model"], "dummy-model")
        self.assertEqual(len(obj["messages"]), 1)

    def test_parse_response_happy_path(self) -> None:
        body = {
            "choices": [
                {"message": {"role": "assistant", "content": "ok"}},
            ],
        }
        data = json.dumps(body).encode("utf-8")
        text = _parse_response(data)
        self.assertEqual(text, "ok")


    def test_parse_response_raises_on_empty_choices(self) -> None:
        body = {"choices": []}
        data = json.dumps(body).encode("utf-8")
        with self.assertRaises(CodexError):
            _parse_response(data)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
