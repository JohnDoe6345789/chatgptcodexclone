"""Tests for backend path helpers (no network)."""

from __future__ import annotations

import unittest
from pathlib import Path

from codex_clone import backend


class BackendPathTests(unittest.TestCase):
    """Verify model path helpers behave sensibly."""

    def test_local_model_path_ends_with_filename(self) -> None:
        path = backend._local_model_path()
        self.assertIsInstance(path, Path)
        self.assertTrue(str(path).endswith(backend.HF_FILE))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
