# Changelog

All notable changes to **r2s** are recorded here with **full Git commit SHAs**.
Verify any entry:

```bash
git cat-file -t <sha>    # expect: commit
git log -1 --oneline <sha>
```

Style: [Keep a Changelog](https://keepachangelog.com/).

---

## [Unreleased]

## [0.2.1] — 2026-09-20

### Added
- First production PyPI publish via Trusted Publishing (`v0.2.1` GitHub Release)

### Changed
- Package version bump 0.2.0 → 0.2.1 (0.2.0 remains on TestPyPI)


**Packaging PR #10 merge tip:** `dc824bcee62f6f9ec92ee6755f2ebe4fa8317588`

### Added
- PyPI packaging metadata (0.2.0), Trusted Publishing workflow, packaged schemas for wheel installs
- `docs/publishing.md` Trusted Publishing checklist

**main tip (after identity harden):** `4bdb13527ad0531e86fd86515f606908d267adb8`

Public hardening tracked in GitHub Issues (social preview, release tags, etc.).

---

## [0.2.0] — 2026-09-20 — reference runtime

| | SHA |
|-|-----|
| Tip (outcome log) | `2133fb986be9c015179f9aedb1203b0f61d13000` |
| Merge (PR #1) | `8eb906635969c28b5d4fa8893587f4452f63a951` |
| Runtime feature | `0f60af7911fd361bdc1549f05a63f399d84712eb` |
| Build-artifact ignore | `72f1fb9875f4586ca0ad3ac4e59a046031d4bd75` |
| PR | https://github.com/ao3575911/r2s/pull/1 |

### Added
- Python package `r2s` (`score`, `should_kill`, `rank`, `handoff`, `load_board` / `load_card`)
- CLI + pytest GitHub Actions workflow
- Cycle 1 ship outcome (`examples/outcome.runtime.example.json`)

### Changed
- Ignore egg-info build artifacts

### Verified object types
```text
8eb906635969c28b5d4fa8893587f4452f63a951  merge
0f60af7911fd361bdc1549f05a63f399d84712eb  feat runtime
72f1fb9875f4586ca0ad3ac4e59a046031d4bd75  chore
2133fb986be9c015179f9aedb1203b0f61d13000  outcome log
```

---

## [0.1.0] — 2026-09-20 — spec contract

| | SHA |
|-|-----|
| Initial spec tree | `9ca117eaa83d2abc18d2d233eb12f6ac6ce21af6` |
| Brand / README / MIT | `a96fd16ff8a461b0fb6d43b5686edfe8a6041613` |
| Cycle 0 outcome + cycle 1 handoff draft | `8b5e0f65c275645be0fbc699ff22a69e53167711` |

### Added
- JSON Schemas: card, board, handoff, outcome, scoring
- `docs/SPEC.md`, examples, MIT license
- Brand assets + professional README
- Cycle 0 ship outcome; cycle 1 runtime handoff packet

### Verified object types
```text
9ca117eaa83d2abc18d2d233eb12f6ac6ce21af6  initial
a96fd16ff8a461b0fb6d43b5686edfe8a6041613  brand harden
8b5e0f65c275645be0fbc699ff22a69e53167711  cycle 0 outcome
```

---

## Identity

| Field | Value |
|-------|--------|
| Repository | https://github.com/ao3575911/r2s |
| Default branch | `main` |
| Owner | [ao3575911](https://github.com/ao3575911) |
| License | MIT |
| Normative contract | `docs/SPEC.md` + `schemas/` |
| Brand mark | ↻ |
| Changelog | this file (SHA-verified) |
| Security | `SECURITY.md` |

