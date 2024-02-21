"""Test module for the string puzzles."""
import unittest
import strings as s

class TestStrings(unittest.TestCase):
    """Test class for the string puzzles."""
    def test_reverse_words(self):
        "Test the `reverse_words` function."
        self.assertEqual('', s.reverse_words(''))
        self.assertEqual('jello', s.reverse_words('jello'))
        self.assertEqual(
            'world sunny hello', s.reverse_words('hello sunny world'))
        self.assertEqual(
            'fun-much-so', s.reverse_words('so-much-fun', '-'))

    def test_palindrome(self):
        "Test the `palindrome` function."
        self.assertTrue(s.palindrome("a"))
        self.assertTrue(s.palindrome("aa"))
        self.assertTrue(s.palindrome("aba"))
        self.assertTrue(s.palindrome("abba"))

        self.assertFalse(s.palindrome("abc"))
        self.assertFalse(s.palindrome("ab"))

    def test_isomorphic(self):
        "Test the `isomorphic` function."
        self.assertTrue(s.isomorphic("aba", "xyx"))
        self.assertTrue(s.isomorphic("aa", "bb"))

        self.assertFalse(s.isomorphic("abb", "xxy"))
        self.assertFalse(s.isomorphic("aba", "xxy"))

    def test_common_prefix(self):
        "Test the `common_prefix` function."
        self.assertEqual(
            "",
            s.common_prefix([])
        )
        self.assertEqual(
            "abc",
            s.common_prefix(["abc"])
        )
        self.assertEqual(
            "a",
            s.common_prefix(["a", "ab", "abc"])
        )
        self.assertEqual(
            "a",
            s.common_prefix(["abc", "ab", "a"])
        )
        self.assertEqual(
            "abc",
            s.common_prefix(["abc", "abc", "abc"])
        )
        self.assertEqual(
            "ab",
            s.common_prefix(["abd", "abc", "abc"])
        )
        self.assertEqual(
            "a",
            s.common_prefix(["abc", "abc", "aec"])
        )

    def test_equal_rotated(self):
        "Test the `equal_rotated` function."
        self.assertTrue(s.equal_rotated("a", "a", 0))
        self.assertTrue(s.equal_rotated("a", "a", 1))
        self.assertTrue(s.equal_rotated("a", "a", 2))
        self.assertTrue(s.equal_rotated("ab", "ba", 1))
        self.assertTrue(s.equal_rotated("aba", "aab", 2))
        self.assertTrue(s.equal_rotated("abba", "baab", 2))

        self.assertFalse(s.equal_rotated("abc", "abc", 1))
        self.assertFalse(s.equal_rotated("ab", "ab", 1))

    def test_first_unique(self):
        "Test the `first_unique` function."
        self.assertEqual("h", s.first_unique("hallo"))
        self.assertEqual("$", s.first_unique("abba"))
        self.assertEqual("u", s.first_unique("babassus"))

    def test_roman_to_decimal(self):
        "Test the `roman_to_decimal` function."
        self.assertEqual(5, s.roman_to_decimal("V"))
        self.assertEqual(4, s.roman_to_decimal("IV"))
        self.assertEqual(1519, s.roman_to_decimal("MDXIX"))

    def test_max_distinct_char_substring(self):
        "Test the `max_distinct_char_substring` function."
        self.assertEqual(1, s.max_distinct_char_substring("aa"))
        self.assertEqual(3, s.max_distinct_char_substring("hallo"))
        self.assertEqual(2, s.max_distinct_char_substring("abba"))
        self.assertEqual(
            10, s.max_distinct_char_substring(
                "aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv"))

    def test_edit_distance(self):
        "Test the `edit_distance` function."
        self.assertEqual(0, s.edit_distance("aa", "aa"))
        self.assertEqual(4, s.edit_distance("hallo", "hey"))
        self.assertEqual(2, s.edit_distance("abba", "baba"))

    def test_largest_palindrome(self):
        "Test the `largest_palindrome` function."
        self.assertEqual("", s.largest_palindrome(""))
        self.assertEqual("a", s.largest_palindrome("a"))
        self.assertEqual("aa", s.largest_palindrome("aa"))
        self.assertEqual("a", s.largest_palindrome("ab"))
        self.assertEqual("a", s.largest_palindrome("abc"))
        self.assertEqual("ll", s.largest_palindrome("hallo"))
        self.assertEqual("aba", s.largest_palindrome("aba"))
        self.assertEqual("abba", s.largest_palindrome("abba"))
        self.assertEqual("bab", s.largest_palindrome("babassus"))
        self.assertEqual("aba", s.largest_palindrome("12aba"))
        self.assertEqual("abba", s.largest_palindrome("12abba"))
        self.assertEqual("aba", s.largest_palindrome("aba12"))
        self.assertEqual("abba", s.largest_palindrome("abba12"))
        self.assertEqual("cd@dc", s.largest_palindrome("12abacd@dc"))
        self.assertEqual("cd@@dc", s.largest_palindrome("12abbacd@@dc"))
        self.assertEqual("cd@dc", s.largest_palindrome("cd@dcaba12"))
        self.assertEqual("cd@@dc", s.largest_palindrome("cd@@dcabba12"))
