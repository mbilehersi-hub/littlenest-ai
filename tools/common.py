"""Shared helpers for WAT tools: project paths, .env loading, and .tmp output.

Usage from another tool:
    from common import require_env, tmp_path, write_json
"""

from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP_DIR = ROOT / ".tmp"

try:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
except ImportError:  # python-dotenv not installed; fall back to the real environment
    pass


def require_env(name: str) -> str:
    """Return an environment variable or exit with a clear message."""
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing {name}. Add it to .env (see .env.example).")
    return value


def tmp_path(*parts: str) -> Path:
    """Path inside .tmp/, creating parent directories as needed."""
    path = TMP_DIR.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def write_json(data, *parts: str) -> Path:
    path = tmp_path(*parts)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    return path


def read_json(*parts: str):
    return json.loads((TMP_DIR.joinpath(*parts)).read_text())
