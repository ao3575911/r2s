<p align="center"><b>xpc</b></p>
<p align="center">hypothesis → protocol → result</p>

<p align="center">
  JSON Schema contract for research experiments.<br/>
  Sibling to <a href="https://github.com/ao3575911/r2s">r2s</a> (rank → ship).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/spec-v0.1.0-5eead4?style=flat-square" alt="spec" />
  <img src="https://img.shields.io/badge/license-MIT-0f1115?style=flat-square" alt="MIT" />
</p>

## What

Normalize one experiment:

| Artifact | Job |
|----------|-----|
| `hypothesis` | Claim + falsifier + metric |
| `protocol` | Steps to test it |
| `result` | pass / fail / inconclusive |
| `run` | Bind one cycle |

Cycle 0 = **schemas + spec only** (no CLI yet).

## Quick start

1. Read [`docs/SPEC.md`](docs/SPEC.md)
2. Copy [`examples/`](examples/)
3. Validate with any JSON Schema 2020-12 validator against [`schemas/`](schemas/)

## Layout

```text
schemas/     hypothesis · protocol · result · run
docs/SPEC.md normative rules
examples/    worked cycle (GDk9 compose adapter)
```

## License

[MIT](LICENSE)
