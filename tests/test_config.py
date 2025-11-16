"""Tests for the configuration module."""

from __future__ import annotations

import os
import unittest

from codex_clone.config import load_config, Config


class ConfigTests(unittest.TestCase):
    """Basic tests for load_config behaviour."""

    def setUp(self) -> None:
        self._old_env = dict(os.environ)

    def tearDown(self) -> None:
        os.environ.clear()
        os.environ.update(self._old_env)

    def test_defaults_are_used(self) -> None:
        os.environ.pop("CODEX_BASE_URL", None)
        os.environ.pop("CODEX_MODEL", None)
        config = load_config()
        self.assertIsInstance(config, Config)
        self.assertEqual(config.base_url, "http://localhost:1234")
        self.assertEqual(config.model, "local-coder")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
