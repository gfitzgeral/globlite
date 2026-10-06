# globlite

Match a whole string against a pattern that only uses `*` and `?`.

`*` is any run of characters. `?` is one character. Dots are literal. `**` is just two stars, not a directory wildcard, and `[abc]` is literal text.

```python
from globlite import match, filter_names, matches_any, count_matches, first_match

match("*.txt", "notes.txt")  # True
match("a?c", "abbc")         # False
filter_names("*.txt", ["notes.txt", "notes.md"])
matches_any("notes.md", ["*.txt", "*.md"])  # True
count_matches("*.txt", ["notes.txt", "notes.md"])  # 1
```

```bash
python -m unittest test_globlite.py
```

MIT
