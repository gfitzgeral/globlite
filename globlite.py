"""Match `*` and `?` globs. No `**` and no character classes."""
from __future__ import annotations

import re


def match(pattern: str, text: str) -> bool:
    return re.fullmatch(_compile(pattern), text) is not None


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
