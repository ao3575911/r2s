<p align="center">
  <img src="docs/brand/icon.png" width="88" alt="r2s" />
</p>

<h1 align="center">r2s</h1>

<p align="center"><b>research → rank → ship</b></p>

<p align="center">
  Schema + CLI that turns research into ranked cards, handoffs, and ship outcomes.
</p>

<p align="center">
  <img src="docs/brand/loop.gif" width="640" alt="Sense → Rank → Handoff → Ship" />
</p>

<p align="center">
  <a href="https://pypi.org/project/r2s/"><img src="https://img.shields.io/pypi/v/r2s?style=flat-square&color=5eead4" alt="PyPI" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0f1115?style=flat-square" alt="MIT" /></a>
  <img src="https://img.shields.io/badge/python-3.11%2B-8b949e?style=flat-square" alt="Python" />
</p>

## Install

```bash
pip install r2s
r2s --help
```

## Loop

| | Artifact | Job |
|-|----------|-----|
| Sense | `card` | Normalize a signal |
| Rank | `board` | Score & kill weak work |
| Handoff | `handoff` | Fixed packet for builders |
| Ship | `outcome` | Did the earn hypothesis hold? |

```text
S = (novelty × evidence × usability × fit) / (hours + compute + blast)
```

## Docs

- Spec → [`docs/SPEC.md`](docs/SPEC.md)
- Schemas → [`schemas/`](schemas/)
- Examples → [`examples/`](examples/)
- Changelog → [`CHANGELOG.md`](CHANGELOG.md)

## License

[MIT](LICENSE)
