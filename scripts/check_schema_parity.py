#!/usr/bin/env python3
"""Fail if repo-root schemas/ and packaged src/r2s/schemas/ diverge.

Normative source of truth: schemas/ at repo root.
Packaged copy must match byte-for-byte so wheels ship the same contract.
"""
from __future__ import annotations

import filecmp
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "schemas"
PKG = ROOT / "src" / "r2s" / "schemas"


def main() -> int:
    if not REPO.is_dir():
        print(f"error: missing normative schemas dir: {REPO}", file=sys.stderr)
        return 2
    if not PKG.is_dir():
        print(f"error: missing packaged schemas dir: {PKG}", file=sys.stderr)
        return 2

    repo_files = sorted(p.name for p in REPO.glob("*.schema.json"))
    pkg_files = sorted(p.name for p in PKG.glob("*.schema.json"))

    errors: list[str] = []
    if repo_files != pkg_files:
        only_repo = sorted(set(repo_files) - set(pkg_files))
        only_pkg = sorted(set(pkg_files) - set(repo_files))
        if only_repo:
            errors.append(f"in schemas/ but not packaged: {', '.join(only_repo)}")
        if only_pkg:
            errors.append(f"packaged but not in schemas/: {', '.join(only_pkg)}")

    for name in sorted(set(repo_files) & set(pkg_files)):
        a, b = REPO / name, PKG / name
        if not filecmp.cmp(a, b, shallow=False):
            errors.append(f"content mismatch: {name}")

    if errors:
        print("schema parity check FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print(
            "\nFix: copy schemas/*.schema.json → src/r2s/schemas/ "
            "(or edit normative schemas/ then sync).",
            file=sys.stderr,
        )
        return 1

    print(f"schema parity OK ({len(repo_files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
