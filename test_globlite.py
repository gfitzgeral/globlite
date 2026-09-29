import unittest

from globlite import filter_names, match


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

    def test_literal_dot(self) -> None:
        self.assertFalse(match("a.c", "abc"))
        self.assertTrue(match("a.c", "a.c"))


if __name__ == "__main__":
    unittest.main()
