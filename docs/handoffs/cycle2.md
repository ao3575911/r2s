# Cycle 2 dogfood — CLI rank → handoff

**Date:** 2026-09-20 (AWST)  
**Runtime:** `r2s` 0.2.1 (editable install)  
**Board:** [`examples/cycle2/board.json`](../../examples/cycle2/board.json)

## Rank (`r2s rank`)

| Rank | Card | Score |
|------|------|------:|
| 1 | `r2s-cycle2-board-artefact` | 0.1034 |
| 2 | `r2s-schema-parity-ci` | 0.0838 |
| 3 | `r2s-prod-pypi-v021` | 0.0275 |

Prod PyPI ranked last while login cool-down blocks Trusted Publisher setup ([#12](https://github.com/ao3575911/r2s/issues/12)).

## Winner handoff

See [`examples/cycle2/handoff.json`](../../examples/cycle2/handoff.json).

**Claim:** commit the cycle-2 board + CLI rank output + handoff as the session dogfood artefact.

## Next (active build slot 2)

`r2s-schema-parity-ci` — CI gate that root `schemas/` and packaged `src/r2s/schemas/` stay identical.
