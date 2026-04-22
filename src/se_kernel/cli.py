"""Command-line interface for se_kernel."""

import argparse

from se_kernel.app import run_show


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="se_kernel",
        description="Inspect Structural Explainability kernel artifacts.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    show_parser = subparsers.add_parser(
        "show",
        help="Show available kernel artifacts.",
    )
    show_parser.add_argument(
        "--kind",
        choices=["all", "identifiers", "constants"],
        default="all",
        help="Artifact subset to display.",
    )

    return parser


def main() -> int:
    """Run the command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "show":
        return run_show(kind=args.kind)

    parser.error(f"Unknown command: {args.command}")
    return 2
