# globlite

Match a whole string against a pattern that only uses `*` and `?`.

`*` is any run of characters. `?` is one character. Dots are literal. `**` is just two stars, not a directory wildcard, and `[abc]` is literal text.

```python
from globlite import match

match("*.txt", "notes.txt")  # True
match("a?c", "abbc")         # False
```

```bash
python -m unittest test_globlite.py
```

MIT
