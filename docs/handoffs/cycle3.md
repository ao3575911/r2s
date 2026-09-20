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

## Next (active build slot 2)

`gdk9-egglog-ci-optional` — CI/tox/pytest marker so egglog bridge tests run when `.[egglog]` is installed and skip cleanly otherwise.

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
