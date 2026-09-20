from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from r2s.validate import validate_instance


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_card(path: str | Path) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, Mapping):
        raise TypeError("card JSON must be an object")
    card = dict(data)
    validate_instance(card, "card.schema.json")
    return card


def load_board(path: str | Path) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, Mapping):
        raise TypeError("board JSON must be an object")
    board = dict(data)
    validate_instance(board, "board.schema.json")
    return board
