from __future__ import annotations

import argparse
import sys
from pathlib import Path

from xpc import ARTIFACTS, __version__
from xpc.validate import validate_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="xpc", description="Experiment contract CLI")
    parser.add_argument("--version", action="version", version=f"xpc {__version__}")
    sub = parser.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="Validate hypothesis/protocol/result/run JSON")
    v.add_argument("paths", nargs="+", type=Path, help="JSON files or directories")
    v.add_argument(
        "--kind",
        choices=ARTIFACTS,
        default=None,
        help="Force artifact kind (default: auto-detect)",
    )

    args = parser.parse_args(argv)
    if args.cmd == "validate":
        return _cmd_validate(args.paths, args.kind)
    return 2


def _cmd_validate(paths: list[Path], kind: str | None) -> int:
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files.extend(sorted(p.glob("*.json")))
        else:
            files.append(p)
    if not files:
        print("no JSON files found", file=sys.stderr)
        return 1
    errors = 0
    for f in files:
        if f.suffix != ".json":
            continue
        try:
            detected = validate_file(f, kind=kind)
            print(f"OK  {f}  ({detected})")
        except Exception as e:
            errors += 1
            print(f"FAIL  {f}  {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
