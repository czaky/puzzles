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

    def test_common_prefix(self):
        "Test the `common_prefix` function."
        self.assertEqual(
            "",
            s.common_prefix([])
        )
        self.assertEqual(
            "a",
            s.common_prefix(["a"])
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
