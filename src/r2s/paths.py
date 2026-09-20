from __future__ import annotations

from pathlib import Path


def _schemas_dir() -> Path:
    """Prefer packaged schemas (wheel/sdist); fall back to repo-root schemas/ in editable checkout."""
    packaged = Path(__file__).resolve().parent / "schemas"
    if packaged.is_dir() and any(packaged.glob("*.schema.json")):
        return packaged
    repo = Path(__file__).resolve().parents[2] / "schemas"
    if repo.is_dir() and any(repo.glob("*.schema.json")):
        return repo
    raise FileNotFoundError(
        "r2s schemas not found (expected package data src/r2s/schemas or repo schemas/)"
    )


SCHEMAS_DIR = _schemas_dir()


def schema_path(name: str) -> Path:
    return SCHEMAS_DIR / name
