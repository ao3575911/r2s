# Publishing `r2s` to PyPI

## Versioning

- Package version lives in `pyproject.toml` and `src/r2s/__init__.py` (`__version__`).
- GitHub release tag should match (`v0.2.0` ↔ `0.2.0`).
- Normative schemas remain at repo-root `schemas/`; the wheel embeds a copy under `src/r2s/schemas/` for install-time validation.

## Trusted Publishing (recommended)

1. Create the PyPI project (first upload may be via TestPyPI).
2. On [PyPI](https://pypi.org) → project **r2s** → **Publishing** → **Add a new publisher**:
   - Owner: `ao3575911`
   - Repository: `r2s`
   - Workflow: `publish.yml`
   - Environment: `pypi`
3. Repeat on [TestPyPI](https://test.pypi.org) with environment `testpypi`.
4. In GitHub → **Settings → Environments**, create `pypi` and `testpypi` (optional protection rules).

## Flows

| Trigger | Target |
|---------|--------|
| `workflow_dispatch` → `testpypi` | TestPyPI |
| `workflow_dispatch` → `pypi` | PyPI (manual) |
| GitHub Release `published` | PyPI |

## Local check before release

```bash
python -m build
twine check dist/*
pip install dist/*.whl
python -c "import r2s; from r2s.paths import SCHEMAS_DIR; print(r2s.__version__, SCHEMAS_DIR)"
```
