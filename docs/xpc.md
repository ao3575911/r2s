<p align="center"><b>xpc</b></p>
<p align="center">hypothesis → protocol → result</p>

<p align="center">
  Experiment contract: JSON Schemas + thin CLI.<br/>
  Sibling to <a href="https://github.com/ao3575911/r2s">r2s</a> (rank → ship).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-0.2.0-5eead4?style=flat-square" alt="0.2.0" />
  <img src="https://img.shields.io/badge/license-MIT-0f1115?style=flat-square" alt="MIT" />
</p>

## Install

```bash
pip install -e ".[dev]"   # from clone; PyPI later
xpc validate examples/gdk9-conserve-vs-naive
```

## Loop

| Artifact | Job |
|----------|-----|
| `hypothesis` | Claim + falsifier + metric |
| `protocol` | Steps to test it |
| `result` | pass / fail / inconclusive |
| `run` | Bind one cycle |

## Dogfood (live GDk9 runs)

1. [`examples/gdk9-conserve-vs-naive/`](examples/gdk9-conserve-vs-naive/) — conserve vs naive (moves 1–5)
2. [`examples/gdk9-keysuite-compose/`](examples/gdk9-keysuite-compose/) — KeySuite Phase B
3. [`examples/gdk9-egglog-dr-bridge/`](examples/gdk9-egglog-dr-bridge/) — egglog DR spike YES + CI

## Spec

[`docs/SPEC.md`](docs/SPEC.md) · [`schemas/`](schemas/)

## License

[MIT](LICENSE)
