from __future__ import annotations

from importlib import resources
from pathlib import Path


def schemas_dir() -> Path:
    """Packaged schemas, else repo-root schemas/ when developing from source."""
    try:
        root = resources.files("xpc").joinpath("schemas")
        if root.is_dir() and any(root.iterdir()):
            return Path(str(root))
    except (TypeError, FileNotFoundError, StopIteration):
        pass
    here = Path(__file__).resolve()
    cand = here.parents[2] / "schemas"
    if cand.is_dir():
        return cand
    raise FileNotFoundError("xpc schemas not found (package data or repo schemas/)")
