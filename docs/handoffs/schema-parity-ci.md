# Handoff: r2s-schema-parity-ci

**Card:** `r2s-schema-parity-ci`  
**Repo:** `ao3575911/r2s`  
**Claim:** CI fails when repo-root `schemas/` and `src/r2s/schemas/` diverge byte-for-byte.

## API / surface
- `scripts/check_schema_parity.py` — exit 0 on match, 1 on drift
- GitHub Actions step in `pytest.yml` before tests
- Pytest: `test_schema_parity_script_exits_zero`

## Non-goals
- No schema content changes
- No PyPI republish required for this PR

## Acceptance
- [x] Script passes on clean tree
- [x] Intentionally diverge one file → script exits 1
- [x] CI runs the check on PRs

## Security
No network; local file compare only.

## Ship outcome

| | |
|-|-|
| PR | [#14](https://github.com/ao3575911/r2s/pull/14) |
| Merge | `f5e9621f19e8f59f97823f2261071aaac30804b3` |
| Result | **ship** |
| Outcome | `examples/outcome.schema-parity.example.json` |
