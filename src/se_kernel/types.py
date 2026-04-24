"""Typed structures for se-kernel artifacts."""

from typing import TypedDict


class ArtifactMeta(TypedDict):
    """Shared artifact metadata."""

    version: str
    status: str


class IdentifierGlobal(TypedDict):
    """Global identifier rules."""

    character_set: str
    case: str
    separator: str
    allow_unicode: bool


class IdentifierKind(TypedDict):
    """Identifier kind definition."""

    summary: str
    pattern: str
    examples: list[str]


class IdentifierRules(TypedDict):
    """Identifier invariant rules."""

    must_be_stable: bool
    must_be_ascii: bool
    must_be_lowercase: bool
    must_use_hyphen_separator: bool
    must_not_embed_semantics: bool


# WHY: TOML key is global, not global_ and global is a Python keyword.
# For direct loaded TOML, use functional syntax instead:
IdentifiersData = TypedDict(
    "IdentifiersData",
    {
        "meta": ArtifactMeta,
        "global": IdentifierGlobal,
        "kind": dict[str, IdentifierKind],
        "rules": IdentifierRules,
    },
)


class ReservedValues(TypedDict):
    """Reserved value list."""

    values: list[str]


class ConstantsData(TypedDict):
    """constants.toml structure."""

    meta: ArtifactMeta
    reserved: dict[str, ReservedValues]
    base_types: dict[str, str]
