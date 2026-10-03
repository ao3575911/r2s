from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_root_and_packaged_schemas_match():
    root = ROOT / "schemas"
    pkg = ROOT / "src" / "xpc" / "schemas"
    root_files = {p.name: p.read_bytes() for p in root.glob("*.schema.json")}
    pkg_files = {p.name: p.read_bytes() for p in pkg.glob("*.schema.json")}
    assert root_files.keys() == pkg_files.keys()
    for name in root_files:
        assert root_files[name] == pkg_files[name], name
