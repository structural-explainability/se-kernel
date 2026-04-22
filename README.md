# se-kernel

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://structural-explainability.github.io/se-kernel/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/se-kernel)
[![Python 3.15+](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/se-kernel/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-kernel/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/structural-explainability/se-kernel/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-kernel/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/structural-explainability/se-kernel/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-kernel/actions/workflows/links.yml)

> Structural Explainability Kernel:
> invariant primitives and structural constants for the SE ecosystem.

## Owns

- invariant concepts that must not drift
- minimal shared vocabulary required by all artifacts

## Includes

### Identity primitives

- canonical identifiers
- stability constraints

### Reference structure

- entity reference patterns

### Minimal invariants

- assumptions used by all specifications

### Shared constants

- reserved keys
- canonical field names
- base types

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

After you get a copy of this repo in your own GitHub account,
open a machine terminal in `Repos` or where you want the project:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/se-kernel

cd se-kernel
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run the module
uv run python -m se_kernel show

# optional individually
uv run python -m se_kernel show --kind all
uv run python -m se_kernel show --kind identifiers
uv run python -m se_kernel show --kind constants

# do chores
npx markdownlint-cli "**/*.md" --fix
uv run python -m ruff format .
uv run python -m ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[LICENSE](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
