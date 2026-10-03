from pathlib import Path

import pytest

from r2s.xpc import __version__
from r2s.xpc.cli import main
from r2s.xpc.validate import detect_kind, validate_file

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples" / "xpc"


def test_version():
    assert __version__ == "0.2.0"


@pytest.mark.parametrize(
    "folder",
    [
        "gdk9-conserve-vs-naive",
        "gdk9-keysuite-compose",
        "gdk9-egglog-dr-bridge",
    ],
)
def test_dogfood_dirs(folder):
    d = EXAMPLES / folder
    for name in ("hypothesis", "protocol", "result", "run"):
        p = d / f"{name}.json"
        assert p.is_file(), p
        assert validate_file(p) == name


def test_cli_validate_dir():
    assert main(["validate", str(EXAMPLES / "gdk9-egglog-dr-bridge")]) == 0


def test_detect_hypothesis():
    import json

    data = json.loads((EXAMPLES / "gdk9-conserve-vs-naive" / "hypothesis.json").read_text())
    assert detect_kind(data) == "hypothesis"


def test_r2s_cli_xpc_subcommand():
    from r2s.cli import main as r2s_main

    assert r2s_main(["xpc", "validate", str(EXAMPLES / "gdk9-egglog-dr-bridge")]) == 0
