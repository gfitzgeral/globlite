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


def unmatched(pattern: str, names: list[str]) -> list[str]:
    return [name for name in names if not match(pattern, name)]


def all_match(pattern: str, names: list[str]) -> bool:
    if not names:
        return False
    return all(match(pattern, name) for name in names)


def none_match(pattern: str, names: list[str]) -> bool:
    return count_matches(pattern, names) == 0


def first_unmatched(pattern: str, names: list[str]) -> str:
    for name in names:
        if not match(pattern, name):
            return name
    return ""


def some_match(pattern: str, names: list[str]) -> bool:
    if not names:
        return False
    found = count_matches(pattern, names)
    return 0 < found < len(names)


def unmatched_count(pattern: str, names: list[str]) -> int:
    return len(unmatched(pattern, names))


def match_gap(pattern: str, names: list[str]) -> int:
    return abs(count_matches(pattern, names) - unmatched_count(pattern, names))


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
