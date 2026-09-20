from __future__ import annotations

from typing import Any, Mapping

from r2s.score import score, should_kill


def rank(board: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Rank cards by descending S, tie-break ascending id.

    Cards that fail kill rules or are unscorable are omitted from the ranked
    list. Among remaining cards, at most ``max_active_builds`` cards with
    status ``build`` are kept (highest S first); other statuses are uncapped
    except by overall sort order for presentation.
    """
    max_builds = int(board.get("max_active_builds") or 2)
    cards = [dict(c) for c in board.get("cards", [])]

    scored: list[tuple[float, str, dict[str, Any]]] = []
    for card in cards:
        killed, _ = should_kill(card)
        if killed:
            continue
        try:
            s = score(card)
        except Exception:
            continue
        scored.append((s, str(card["id"]), card))

    scored.sort(key=lambda t: (-t[0], t[1]))

    result: list[dict[str, Any]] = []
    builds = 0
    for s, _id, card in scored:
        if card.get("status") == "build":
            if builds >= max_builds:
                continue
            builds += 1
        result.append(card)
    return result
