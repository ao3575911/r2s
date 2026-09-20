class R2SError(Exception):
    """Base error for the r2s runtime."""


class ValidationError(R2SError):
    """JSON failed schema validation."""


class ScoreError(R2SError):
    """Card cannot be scored (e.g. zero denominator)."""


class KillError(R2SError):
    """Reserved for kill-path helpers."""
