import unittest

from globlite import all_match, count_matches, filter_names, first_match, first_unmatched, match, match_gap, matches_any, none_match, some_match, unmatched, unmatched_count, any_left


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
        self.assertFalse(all_match("*.txt", names))
        self.assertTrue(all_match("*.txt", ["notes.txt", "a.txt"]))
        self.assertTrue(none_match("*.png", names))
        self.assertFalse(none_match("*.txt", names))
        self.assertEqual(first_unmatched("*.txt", names), "notes.md")
        self.assertEqual(first_unmatched("*.txt", ["notes.txt", "a.txt"]), "")
        self.assertTrue(some_match("*.txt", names))
        self.assertFalse(some_match("*.png", names))
        self.assertEqual(unmatched_count("*.txt", names), 1)
        self.assertEqual(match_gap("*.txt", names), 1)
        self.assertTrue(any_left("*.txt", names))
        self.assertFalse(any_left("*.txt", ["notes.txt", "a.txt"]))

    def test_literal_dot(self) -> None:
        self.assertFalse(match("a.c", "abc"))
        self.assertTrue(match("a.c", "a.c"))


if __name__ == "__main__":
    unittest.main()
