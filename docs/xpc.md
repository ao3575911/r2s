<p align="center"><b>xpc</b></p>
<p align="center">hypothesis → protocol → result</p>

<p align="center">
  Experiment contract: JSON Schemas + thin CLI.<br/>
  Sibling to <a href="https://github.com/ao3575911/r2s">r2s</a> (rank → ship).
</p>

<p align="center">
  <a href="https://pypi.org/project/xpc/"><img src="https://img.shields.io/pypi/v/xpc?style=flat-square&color=5eead4" alt="PyPI" /></a>
  <img src="https://img.shields.io/badge/python-3.11%2B-8b949e?style=flat-square" alt="Python" />
  <img src="https://img.shields.io/badge/license-MIT-0f1115?style=flat-square" alt="MIT" />
</p>

## Install

```bash
pip install xpc
xpc validate examples/gdk9-conserve-vs-naive
```

From a clone (dev):

```bash
pip install -e ".[dev]"
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

## Publish

Trusted Publishing (OIDC): [`.github/workflows/publish.yml`](.github/workflows/publish.yml) · checklist [`docs/PUBLISHING.md`](docs/PUBLISHING.md)

## Spec

[`docs/SPEC.md`](docs/SPEC.md) · [`schemas/`](schemas/)

## License

[MIT](LICENSE)
