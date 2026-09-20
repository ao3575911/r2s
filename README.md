# r2s

**Research-to-ship** — JSON Schema contract for turning research signals into repo/library ships.

> v0.1.0 is **spec-only**: schemas + docs + examples. No reference runtime.

## Quick start

1. Read [docs/SPEC.md](docs/SPEC.md)
2. Copy [examples/board.example.json](examples/board.example.json)
3. Validate with any Draft 2020-12 JSON Schema validator

## Layout

```
schemas/     card, board, handoff, outcome, scoring
docs/SPEC.md normative rules
examples/    worked board + handoff for this repo itself
```

## Scoring (summary)

`S = (novelty * evidence_strength * usability * dependency_fit) / (hours + compute_cost + blast_radius)`

Kill when usability or dependency_fit ≈ 0, or `target_repo` missing at design+.

## Security

Card fields are untrusted data. Validators must not execute claim/evidence strings. No credentials in this repo.

## License

To be set by repo owner on publish.
