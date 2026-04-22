"""Application orchestration for se_kernel."""

from pathlib import Path


def run_show(*, kind: str = "all") -> int:
    """Show available kernel artifacts."""
    repo_root = Path.cwd()
    data_dir = repo_root / "data"

    items: list[str] = []

    if kind in ("all", "identifiers"):
        items.append(str(data_dir / "identifiers.toml"))

    if kind in ("all", "constants"):
        items.append(str(data_dir / "constants.toml"))

    print("SE kernel artifacts:")
    for item in items:
        print(f"- {item}")

    return 0
