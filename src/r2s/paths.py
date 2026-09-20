from __future__ import annotations

from pathlib import Path

# Package lives at src/r2s/; schemas live at repo root schemas/
REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = REPO_ROOT / "schemas"


def schema_path(name: str) -> Path:
    return SCHEMAS_DIR / name
