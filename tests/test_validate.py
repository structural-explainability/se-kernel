"""Validation tests for se-kernel artifacts."""

from typing import Any, cast

from se_kernel.types import ConstantsData, IdentifiersData
from se_kernel.validate import validate_constants, validate_identifiers


def make_valid_identifiers() -> IdentifiersData:
    """Return valid identifiers data."""
    return {
        "meta": {"version": "0.1.0", "status": "draft"},
        "global": {
            "character_set": "ascii-lower-hyphen",
            "case": "lower",
            "separator": "-",
            "allow_unicode": False,
        },
        "kind": {
            "repo": {
                "summary": "Canonical repository identifier.",
                "pattern": "se-{name}",
                "examples": ["se-kernel"],
            }
        },
        "rules": {
            "must_be_stable": True,
            "must_be_ascii": True,
            "must_be_lowercase": True,
            "must_use_hyphen_separator": True,
            "must_not_embed_semantics": True,
        },
    }


def make_valid_constants() -> ConstantsData:
    """Return valid constants data."""
    return {
        "meta": {"version": "0.1.0", "status": "draft"},
        "reserved": {
            "repo_classes": {"values": ["constitution", "kernel"]},
        },
        "base_types": {
            "identifier": "string",
            "string_list": "list[string]",
        },
    }


def test_validate_identifiers_accepts_valid_data() -> None:
    """Valid identifiers data should produce no errors."""
    errors = validate_identifiers(make_valid_identifiers())
    assert errors == []


def test_validate_identifiers_requires_kind_entries() -> None:
    """Identifier kinds must not be empty."""
    data = make_valid_identifiers()
    data["kind"] = {}

    errors = validate_identifiers(data)

    assert "identifiers.toml: [kind] must not be empty." in errors


def test_validate_identifiers_requires_summary_pattern_and_examples() -> None:
    """Identifier kinds must define summary, pattern, and examples."""
    data = cast(dict[str, Any], make_valid_identifiers())
    data["kind"]["repo"] = {"summary": "", "pattern": "", "examples": []}

    errors = validate_identifiers(cast(IdentifiersData, data))

    assert "identifiers.toml: [kind.repo] must define summary." in errors
    assert "identifiers.toml: [kind.repo] must define pattern." in errors
    assert "identifiers.toml: [kind.repo] must define examples." in errors


def test_validate_constants_accepts_valid_data() -> None:
    """Valid constants data should produce no errors."""
    errors = validate_constants(make_valid_constants())
    assert errors == []


def test_validate_constants_requires_reserved_values() -> None:
    """Reserved groups must define values."""
    data = make_valid_constants()
    data["reserved"]["repo_classes"] = {"values": []}

    errors = validate_constants(data)

    assert "constants.toml: [reserved.repo_classes] must define values." in errors


def test_validate_constants_requires_base_types() -> None:
    """Base types must not be empty."""
    data = make_valid_constants()
    data["base_types"] = {}

    errors = validate_constants(data)

    assert "constants.toml: [base_types] must not be empty." in errors
