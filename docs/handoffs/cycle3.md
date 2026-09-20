# Cycle 3 dogfood — GDk9 second consumer

**Date:** 2026-09-20 (AWST)  
**Runtime:** `r2s` editable install (`/tmp/r2s-c3`)  
**Board:** [`examples/cycle3/board.json`](../../examples/cycle3/board.json)  
**Target consumer:** [`ao3575911/gdk9`](https://github.com/ao3575911/gdk9) (package `gdk9-cli` 0.3.0)

This cycle is **not** another self-card about r2s packaging. The board is the r2s artefact; the winning card is a GDk9 implementation handoff.

## Rank (`r2s rank`)

| Rank | Card | Score |
|------|------|------:|
| 1 | `gdk9-conserve-move5` | 0.0934 |
| 2 | `gdk9-egglog-ci-optional` | 0.0779 |
| 3 | `gdk9-trusted-publish` | 0.0285 |
| 4 | `gdk9-keysuite-phase-b-spike` | 0.0204 |

## Winner claim

**Card:** `gdk9-conserve-move5`  
**Claim:** Add conserve-search move 5 as a failing-first pytest that extends `EXPERIMENT_CONSERVE_SEARCH` (multi-step fuse/split chain or depth-bounded reject of a new naive-accepts/kernel-rejects beat).

See [`examples/cycle3/handoff.json`](../../examples/cycle3/handoff.json).

**Implementation owner:** GDk9 bot (id `1398231`) / repo `ao3575911/gdk9` — **do not** implement gdk9 code in this r2s PR.

## Next (active build slot 2) — **handed off**

`gdk9-egglog-ci-optional` — CI/tox/pytest marker so egglog bridge tests run when `.[egglog]` is installed and skip cleanly otherwise.

Handoff packet: [`examples/cycle3/handoff.egglog.json`](../../examples/cycle3/handoff.egglog.json) (card: [`examples/cycle3/next.card.json`](../../examples/cycle3/next.card.json)).

## Non-goals (this artefact PR)

- No gdk9 source, test, or workflow changes in `ao3575911/r2s`
- No Trusted Publishing / KeySuite Phase B / egglog CI implementation here
- No new r2s schema or runtime behavior changes
- No secrets in board/handoff strings

## Evidence snapshot (live GDk9)

- Recent merges: PR#18 handbook kernel CLI doctest gate; PR#17 conserve move 4; PR#16 move 3; AGPL license
- `docs/EXPERIMENT_CONSERVE_SEARCH.md` — move 4 done; next beat not coded
- `docs/SPIKE-egglog.md` + `gdk9/egglog_bridge/` — optional egglog spike
- `docs/KEYSUITE_BRIDGE.md` — Phase A docs-only
- `docs/RELEASE.md` — local/TestPyPI path; no Trusted Publishing workflow yet
- No open issues on gdk9 at board time

## Cycle 3 ship (verified)

| | |
|-|-|
| PR | [#15](https://github.com/ao3575911/r2s/pull/15) |
| Merge commit | `bde60953bce7a3314feec61591aa1b73b5c55145` |
| Outcome | [`examples/outcome.cycle3.example.json`](../../examples/outcome.cycle3.example.json) |
| Result | **ship** (artefact only; GDk9 implementation deferred to bot 1398231) |

## GDk9 implementation ship

Conserve-search Move 5 landed in `ao3575911/gdk9` after the cycle3 handoff.

| | |
|-|-|
| PR | [#19](https://github.com/ao3575911/gdk9/pull/19) |
| Merge commit | `bc58029380db04fe76a7c2cce7819734331a3fbe` |
| Outcome | [`examples/outcome.gdk9-conserve-move5.example.json`](../../examples/outcome.gdk9-conserve-move5.example.json) |
| Result | **ship** (GDk9 bot implementation; fuse→split→fuse + same-names mismatch; Moves 1–4 green) |

**Next slot:** `gdk9-egglog-ci-optional` is **handed off** — see [`examples/cycle3/handoff.egglog.json`](../../examples/cycle3/handoff.egglog.json).
