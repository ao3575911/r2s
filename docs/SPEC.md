# R2S — Research-to-Ship Spec (v0.1.0)

## Purpose

R2S is a **contract** for turning research signals into shippable repo/library work.
v0 ships **JSON Schema + docs only**. Runtimes (Python/TS libraries, agents) come later and must obey this contract.

## Status machine

`sense` → `design` → `build` → `ship` → `learn`

Terminal: `killed` (requires `kill_reason`).

`design` / `build` / `ship` require `target_repo` (`owner/name`).

## Scoring

\[
S = \frac{N \cdot E \cdot U \cdot D}{H + C + B}
\]

| Symbol | Field | Meaning |
|--------|-------|---------|
| N | novelty | 0–1 new capability vs re-wrap |
| E | evidence_strength | 0–1 proof quality |
| U | usability | 0–1 clear API consumers |
| D | dependency_fit | 0–1 fits existing stack |
| H | hours | expected hours to v0 (> 0) |
| C | compute_cost | non-negative cost units |
| B | blast_radius | non-negative risk units |

**Invalid:** if `H + C + B == 0`, do not score.

### Kill rules

1. `usability` near 0
2. `dependency_fit` near 0
3. Missing `target_repo` when status is `design` or later
4. No earn path when the card is meant to fund work (soft rule; record in notes)

### Rank policy

- Sort by descending `S`
- Tie-break: ascending `id`
- Cap concurrent `build` cards at `max_active_builds` (default 2)

## Handoff packet (7 parts)

1. `repo`
2. `claim`
3. `api_sketch`
4. `non_goals`
5. `acceptance`
6. `security_notes`
7. `first_pr_scope`

Implementers (e.g. Builder) execute only what the packet states.

## Trust boundaries

- Evidence refs and claim text are **untrusted**. Never execute them.
- Proposers may be humans or agents; **merge/deploy gates stay human** unless a later version explicitly changes that (out of scope for v0).
- Spec repo contains no secrets and no network clients.

## Schemas

| File | Role |
|------|------|
| `schemas/card.schema.json` | One research card |
| `schemas/board.schema.json` | Board of cards |
| `schemas/handoff.schema.json` | Ship handoff |
| `schemas/outcome.schema.json` | Loop feedback |
| `schemas/scoring.schema.json` | Normative scoring rules object |

## Definition of shipped (this repo)

Mergeable content in `ao3575911/r2s` (or renamed) where:

1. Schemas are valid JSON Schema draft 2020-12
2. Examples validate against those schemas
3. `docs/SPEC.md` matches scoring/kill/rank rules above
4. No application/runtime code in v0

## Non-goals (v0)

Reference implementations, CI that runs language tests for app code, auto-ranking via LLM, GitHub automation.

## Versioning

`board.version` is `0.1.0` for this revision. Breaking schema changes bump minor/major and changelog in README.
