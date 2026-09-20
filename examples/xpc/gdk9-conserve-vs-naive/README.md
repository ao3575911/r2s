# Dogfood: GDk9 conserved search vs naive join/split

Real experiment (not a toy). Sourced from:

- https://github.com/ao3575911/gdk9/blob/main/docs/EXPERIMENT_CONSERVE_SEARCH.md
- https://github.com/ao3575911/gdk9/pull/19 (move 5 merge)

| File | Role |
|------|------|
| `hypothesis.json` | Bounded validity claim |
| `protocol.json` | Moves 1–5 method |
| `result.json` | pass @ `bc580293…` |
| `run.json` | Complete cycle binder |

Validate:

```bash
# any Draft 2020-12 validator against ../../schemas/*.schema.json
```
