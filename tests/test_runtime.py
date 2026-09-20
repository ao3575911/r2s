from __future__ import annotations

import math
from pathlib import Path

import pytest

from r2s.errors import ScoreError, ValidationError
from r2s.handoff import handoff
from r2s.io import load_board
from r2s.rank import rank
from r2s.score import score, should_kill
from r2s.validate import validate_instance

ROOT = Path(__file__).resolve().parents[1]
BOARD = ROOT / "examples" / "board.example.json"


def test_score_formula():
    card = {
        "novelty": 0.4,
        "evidence_strength": 0.7,
        "usability": 0.9,
        "dependency_fit": 0.95,
        "hours": 4,
        "compute_cost": 0,
        "blast_radius": 1,
    }
    expected = (0.4 * 0.7 * 0.9 * 0.95) / (4 + 0 + 1)
    assert math.isclose(score(card), expected)


def test_score_zero_denominator():
    card = {
        "novelty": 1,
        "evidence_strength": 1,
        "usability": 1,
        "dependency_fit": 1,
        "hours": 0,
        "compute_cost": 0,
        "blast_radius": 0,
    }
    # hours has exclusiveMinimum 0 in schema, but score must still guard
    with pytest.raises(ScoreError):
        score(card)


def test_should_kill_rules():
    base = {
        "id": "x",
        "claim": "c",
        "evidence": [],
        "novelty": 0.5,
        "evidence_strength": 0.5,
        "usability": 0.5,
        "dependency_fit": 0.5,
        "hours": 1,
        "compute_cost": 0,
        "blast_radius": 1,
        "status": "sense",
    }
    assert should_kill({**base, "usability": 0})[0] is True
    assert should_kill({**base, "dependency_fit": 0})[0] is True
    assert should_kill({**base, "status": "design"})[0] is True
    assert should_kill({**base, "status": "design", "target_repo": "a/b"})[0] is False


def test_rank_and_handoff_roundtrip():
    board = load_board(BOARD)
    ranked = rank(board)
    assert ranked, "expected at least one live card"
    top = ranked[0]
    assert top["id"] == "r2s-spec-v0"
    packet = handoff(
        top,
        draft={
            "api_sketch": "schemas + docs",
            "non_goals": ["No runtime in this card"],
            "acceptance": ["Examples validate"],
            "security_notes": ["Untrusted card strings"],
            "first_pr_scope": "Spec only",
        },
    )
    validate_instance(packet, "handoff.schema.json")
    assert packet["repo"] == top["target_repo"]
    assert packet["claim"] == top["claim"]


def test_rank_tie_break_and_build_cap():
    board = {
        "version": "0.1.0",
        "max_active_builds": 1,
        "cards": [
            _card("b", 0.5, "build"),
            _card("a", 0.5, "build"),
            _card("c", 0.9, "design"),
        ],
    }
    ranked = rank(board)
    ids = [c["id"] for c in ranked]
    # c first (higher score), then one build (a before b on tie of remaining builds by id)
    assert ids[0] == "c"
    build_ids = [c["id"] for c in ranked if c["status"] == "build"]
    assert len(build_ids) == 1
    assert build_ids[0] == "a"


def _card(cid: str, s_factor: float, status: str) -> dict:
    # Arrange inputs so score ordering follows s_factor via novelty
    return {
        "id": cid,
        "claim": "claim",
        "evidence": [],
        "novelty": s_factor,
        "evidence_strength": 1,
        "usability": 1,
        "dependency_fit": 1,
        "hours": 1,
        "compute_cost": 0,
        "blast_radius": 0,
        "status": status,
        "target_repo": "ao3575911/r2s",
    }


def test_import_r2s():
    import r2s

    assert r2s.__version__ == "0.2.1"


def test_packaged_schemas_match_repo_root():
    import filecmp
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    pkg = root / "src" / "r2s" / "schemas"
    repo = root / "schemas"
    pkg_files = sorted(p.name for p in pkg.glob("*.schema.json"))
    repo_files = sorted(p.name for p in repo.glob("*.schema.json"))
    assert pkg_files == repo_files
    for name in pkg_files:
        assert filecmp.cmp(pkg / name, repo / name, shallow=False)


def test_schema_parity_script_exits_zero():
    import subprocess
    import sys
    from pathlib import Path

    script = Path(__file__).resolve().parents[1] / "scripts" / "check_schema_parity.py"
    r = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "schema parity OK" in r.stdout
