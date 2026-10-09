import unittest

from globlite import count_matches, filter_names, first_match, match, matches_any, unmatched


class GlobliteTest(unittest.TestCase):
    def test_star_and_question(self) -> None:
        self.assertTrue(match("a*c", "abc"))
        self.assertTrue(match("a*c", "abXc"))
        self.assertTrue(match("a?c", "abc"))
        self.assertFalse(match("a?c", "abbc"))
        self.assertFalse(match("*.txt", "notes.md"))

    def test_filter(self) -> None:
        names = ["notes.txt", "notes.md", "a.txt"]
        self.assertEqual(filter_names("*.txt", names), ["notes.txt", "a.txt"])
        self.assertTrue(matches_any("notes.md", ["*.txt", "*.md"]))
        self.assertFalse(matches_any("notes.md", ["*.txt"]))
        self.assertEqual(count_matches("*.txt", names), 2)
        self.assertEqual(first_match("*.txt", names), "notes.txt")
        self.assertEqual(first_match("*.png", names), "")
        self.assertEqual(unmatched("*.txt", names), ["notes.md"])

    def test_literal_dot(self) -> None:
        self.assertFalse(match("a.c", "abc"))
        self.assertTrue(match("a.c", "a.c"))


if __name__ == "__main__":
    unittest.main()
