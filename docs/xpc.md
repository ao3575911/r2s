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

| Artifact | Job |
|----------|-----|
| `hypothesis` | Claim + falsifier + metric |
| `protocol` | Steps to test it |
| `result` | pass / fail / inconclusive |
| `run` | Bind one cycle |

## Dogfood

Real GDk9 experiment (conserved search vs naive join/split, moves 1–5):

[`examples/gdk9-conserve-vs-naive/`](examples/gdk9-conserve-vs-naive/)

Also: [`examples/gdk9-keysuite-compose/`](examples/gdk9-keysuite-compose/) (Phase B compose adapter).

## Quick start

1. [`docs/SPEC.md`](docs/SPEC.md)
2. Copy an [`examples/`](examples/) cycle
3. Validate against [`schemas/`](schemas/) (JSON Schema 2020-12)

## License

[MIT](LICENSE)
