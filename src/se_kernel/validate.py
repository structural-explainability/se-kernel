"""Validation for se-kernel artifacts."""

from se_kernel.types import ConstantsData, IdentifiersData


def validate_identifiers(data: IdentifiersData) -> list[str]:
    """Validate identifiers.toml structure."""
    errors: list[str] = []

    if not data["kind"]:
        errors.append("identifiers.toml: [kind] must not be empty.")

    for kind_name, kind_def in data["kind"].items():
        if not kind_def.get("summary", "").strip():
            errors.append(f"identifiers.toml: [kind.{kind_name}] must define summary.")

        if not kind_def.get("pattern", "").strip():
            errors.append(f"identifiers.toml: [kind.{kind_name}] must define pattern.")

        examples = kind_def.get("examples", [])
        if not examples:
            errors.append(f"identifiers.toml: [kind.{kind_name}] must define examples.")

    return errors


def validate_constants(data: ConstantsData) -> list[str]:
    """Validate constants.toml structure."""
    errors: list[str] = []

    if not data["reserved"]:
        errors.append("constants.toml: [reserved] must not be empty.")

    for group_name, group_def in data["reserved"].items():
        values = group_def.get("values", [])
        if not values:
            errors.append(
                f"constants.toml: [reserved.{group_name}] must define values."
            )

    if not data["base_types"]:
        errors.append("constants.toml: [base_types] must not be empty.")

    return errors
