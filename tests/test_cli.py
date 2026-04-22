"""Minimal CLI smoke tests for se_kernel."""

from se_kernel.app import run_show


def test_run_show_returns_success() -> None:
    """run_show should return 0 for default invocation."""
    rc = run_show(kind="all")
    assert rc == 0


def test_run_show_identifiers() -> None:
    """run_show should handle identifiers subset."""
    rc = run_show(kind="identifiers")
    assert rc == 0


def test_run_show_constants() -> None:
    """run_show should handle constants subset."""
    rc = run_show(kind="constants")
    assert rc == 0
