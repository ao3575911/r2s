"""r2s — reference runtime for the research-to-ship schema contract."""

from r2s.errors import KillError, ScoreError, ValidationError
from r2s.handoff import handoff
from r2s.io import load_board, load_card, load_json
from r2s.rank import rank
from r2s.score import score, should_kill

__all__ = [
    "KillError",
    "ScoreError",
    "ValidationError",
    "handoff",
    "load_board",
    "load_card",
    "load_json",
    "rank",
    "score",
    "should_kill",
]

__version__ = "0.2.0"
