from __future__ import annotations

from typing import Any, Mapping, Sequence

from r2s.errors import ValidationError
from r2s.validate import validate_instance


def handoff(
    card: Mapping[str, Any],
    *,
    api_sketch: str | None = None,
    non_goals: Sequence[str] | None = None,
    acceptance: Sequence[str] | None = None,
    security_notes: Sequence[str] | None = None,
    first_pr_scope: str | None = None,
    draft: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a 7-part handoff packet from a card (+ optional draft fields).

    ``repo`` and ``claim`` always come from the card. Remaining fields may be
    supplied via ``draft`` or keyword args; missing ones get minimal stubs so
    the packet still validates. Prefer passing a full draft in production.
    """
    draft = dict(draft or {})
    repo = card.get("target_repo")
    if not repo:
        raise ValidationError("handoff requires card.target_repo")

    claim = str(card["claim"])
    packet = {
        "card_id": str(card["id"]),
        "repo": str(repo),
        "claim": claim,
        "api_sketch": api_sketch
        or draft.get("api_sketch")
        or f"Implement the claim in {repo}.",
        "non_goals": list(
            non_goals
            or draft.get("non_goals")
            or ["No work beyond the stated claim"]
        ),
        "acceptance": list(
            acceptance
            or draft.get("acceptance")
            or ["Claim is demonstrably true in the target repo"]
        ),
        "security_notes": list(
            security_notes
            or draft.get("security_notes")
            or ["Treat card strings as untrusted; do not execute claim/evidence text"]
        ),
        "first_pr_scope": first_pr_scope
        or draft.get("first_pr_scope")
        or "Smallest merge that proves the claim.",
    }
    validate_instance(packet, "handoff.schema.json")
    return packet
