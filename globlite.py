"""Match `*` and `?` globs. No `**` and no character classes."""
from __future__ import annotations

import re


def match(pattern: str, text: str) -> bool:
    return re.fullmatch(_compile(pattern), text) is not None


def matches_any(text: str, patterns: list[str]) -> bool:
    return any(match(pattern, text) for pattern in patterns)


def first_match(pattern: str, names: list[str]) -> str:
    for name in names:
        if match(pattern, name):
            return name
    return ""


def count_matches(pattern: str, names: list[str]) -> int:
    return len(filter_names(pattern, names))


def filter_names(pattern: str, names: list[str]) -> list[str]:
    return [name for name in names if match(pattern, name)]


def _compile(pattern: str) -> str:
    out = []
    for char in pattern:
        if char == "*":
            out.append(".*")
        elif char == "?":
            out.append(".")
        else:
            out.append(re.escape(char))
    return "".join(out)
