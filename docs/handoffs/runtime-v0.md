# Handoff: r2s reference runtime (cycle 1)

**Card:** `r2s-runtime-v0`  
**Repo:** `ao3575911/r2s`  
**Machine-readable twin:** [`examples/handoff.runtime.example.json`](../../examples/handoff.runtime.example.json)

## 1. Repo
`ao3575911/r2s` — branch `feat/runtime-v0` → PR into `main`.

## 2. Claim
A caller can load a board, score and rank cards per SPEC, apply kill rules, and emit a 7-part handoff packet — with no network I/O and no LLM calls.

## 3. API sketch
Python 3.11+ package `r2s`:

| Symbol | Behavior |
|--------|----------|
| `score(card) -> float` | SPEC formula; error/invalid if `H+C+B == 0` |
| `should_kill(card) -> tuple[bool, str\|None]` | Kill rules from SPEC |
| `rank(board) -> list[Card]` | Descending `S`, tie-break ascending `id`; respect `max_active_builds` |
| `handoff(card) -> HandoffPacket` | 7 fields; validate against `handoff.schema.json` |
| `load_board(path) -> Board` | JSON + schema validate |

Optional CLI: `r2s rank board.json`, `r2s handoff card.json`.

## 4. Non-goals
- No GitHub / git write / auto-PR  
- No LLM or agent runtime  
- No network I/O in library code  
- No secrets  
- No SPEC changes (implement only)  
- No TS port in this PR  

## 5. Acceptance
- `pytest` green  
- Formula + kill + rank semantics match `../SPEC.md`  
- `handoff()` output validates against `schemas/handoff.schema.json`  
- `examples/board.example.json` round-trips (load → rank → handoff)  
- `pip install -e ".[dev]"`; `import r2s` works  
- Unit tests make no network calls  

## 6. Security notes
- Card strings are untrusted — never `eval` / shell / fetch evidence refs  
- Pin deps; prefer stdlib + `jsonschema` (or pydantic)  
- No env-secret reads in library  

## 7. First PR scope
`src/r2s/`, `tests/`, `pyproject.toml`, optional CLI, basic GitHub Actions `pytest`. Schemas remain normative.

## Prior outcome (cycle 0)
See [`examples/outcome.example.json`](../../examples/outcome.example.json) — `r2s-spec-v0` → **ship**.

## Cycle 1 outcome

**ship** — merged https://github.com/ao3575911/r2s/pull/1 at 2026-09-20T13:01:11Z. See [`examples/outcome.runtime.example.json`](../../examples/outcome.runtime.example.json).

## Cycle 1 ship (verified)

| | |
|-|-|
| PR | [#1](https://github.com/ao3575911/r2s/pull/1) |
| Merge commit | `8eb906635969c28b5d4fa8893587f4452f63a951` |
| Feature commit | `0f60af7911fd361bdc1549f05a63f399d84712eb` |
| Outcome commit | `2133fb986be9c015179f9aedb1203b0f61d13000` |
| Outcome file | [`examples/outcome.runtime.example.json`](../../examples/outcome.runtime.example.json) |
