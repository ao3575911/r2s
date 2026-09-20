from __future__ import annotations

from typing import Any, Mapping

from r2s.errors import ScoreError

# Kill threshold: "near 0" in SPEC — treat values <= epsilon as near zero.
_NEAR_ZERO = 1e-9
_DESIGN_PLUS = frozenset({"design", "build", "ship"})


def score(card: Mapping[str, Any]) -> float:
    """Return S = (N*E*U*D) / (H+C+B). Raises ScoreError if denominator is 0."""
    n = float(card["novelty"])
    e = float(card["evidence_strength"])
    u = float(card["usability"])
    d = float(card["dependency_fit"])
    h = float(card["hours"])
    c = float(card["compute_cost"])
    b = float(card["blast_radius"])
    denom = h + c + b
    if denom == 0:
        raise ScoreError("hours + compute_cost + blast_radius == 0; card is unscorable")
    return (n * e * u * d) / denom


def should_kill(card: Mapping[str, Any]) -> tuple[bool, str | None]:
    """Apply SPEC kill rules. Returns (killed?, reason)."""
    if float(card["usability"]) <= _NEAR_ZERO:
        return True, "usability near 0"
    if float(card["dependency_fit"]) <= _NEAR_ZERO:
        return True, "dependency_fit near 0"
    status = card["status"]
    if status in _DESIGN_PLUS and not card.get("target_repo"):
        return True, "missing target_repo at design+"
    return False, None
