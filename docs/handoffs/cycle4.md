# Cycle 4 handoff — r2s

**Date:** 2026-09-21 (Australia/Perth)  
**Board:** `examples/cycle4/board.json`  
**Rank:** `examples/cycle4/rank.out.json`  
**Winner handoff:** `examples/cycle4/handoff.json`  
**Winner card:** `examples/cycle4/top.card.json`

## Rank order

| # | Card | Score | Target |
|---|------|-------|--------|
| 1 | `r2s-xpc-run-link` | 0.0857 | ao3575911/r2s |
| 2 | `r2s-validate-board-cli` | 0.0606 | ao3575911/r2s |
| 3 | `gdk9-keysuite-fsm-slice` | 0.0449 | ao3575911/gdk9 |
| 4 | `xpc-pypi-v020` | 0.0443 | ao3575911/xpc |

`max_active_builds: 2` → build **r2s-xpc-run-link** first, then **r2s-validate-board-cli**.

## Why these cards (live only)

- **xpc PyPI** — `publish.yml` already on main; `pypi.org/pypi/xpc` still 404. Blocked on Adam pending publishers, not engineering hours. Formula scored it lower (low novelty / blast radius), but it remains the highest *external* unlock once UI is done.
- **r2s ↔ xpc link** — three live xpc dogfood runs exist; outcomes cannot cite them yet.
- **validate CLI** — parity with `xpc validate`; reduces silent schema drift mid-cycle.
- **KeySuite FSM slice** — honest next GDk9 research beat after Phase B (#22).

## Non-goals this cycle

- No website / Pages (#4 stays deferred)
- No r2s feature inflation / SaaS
- No inventing filler cards

## Next actions

1. Merge this cycle-4 artefact tree.
2. Implement winner: optional `xpc_run_id` on outcome schema + example.
3. Queue `r2s validate` CLI as second active build.
4. When Adam finishes xpc publishers → dry-run TestPyPI → tag `v0.2.0` (card `xpc-pypi-v020`).
