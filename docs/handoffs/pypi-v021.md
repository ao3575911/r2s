# Handoff: prod PyPI `r2s==0.2.1`

## Result
**ship** — published to https://pypi.org/project/r2s/0.2.1/

## How
1. Trusted Publisher on pypi.org (Owner `ao3575911`, Repo `r2s`, Workflow `publish.yml`, Environment `pypi`)
2. `gh workflow run publish.yml -f target=pypi`
3. Run https://github.com/ao3575911/r2s/actions/runs/35517936926

## Verify
```bash
pip install r2s==0.2.1
python -c "import r2s; print(r2s.__version__)"
```

## Tracker
Issue #12 closed.
