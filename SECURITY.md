# Security

## Trust model

Card fields (claim, evidence refs, notes) are **untrusted data**. Validators and the reference runtime must not execute or fetch them.

## Reporting

Open a private security advisory on this GitHub repository, or contact the owner via GitHub.

## Supply chain

- Pin runtime dependencies in `pyproject.toml`
- Prefer Dependabot security updates once enabled (see open issues)
- Secret scanning and push protection are enabled on the repo

## Verified commits

Public ship points are listed with full SHAs in [`CHANGELOG.md`](CHANGELOG.md). Confirm with `git cat-file -t <sha>`.
