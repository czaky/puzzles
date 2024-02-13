import unittest
from strings import *

class TestStrings(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual('', reverse_words(''))
        self.assertEqual('jello', reverse_words('jello'))
        self.assertEqual(
            'world sunny hello', reverse_words('hello sunny world'))
        self.assertEqual(
            'fun-much-so', reverse_words('so-much-fun', '-'))

    def test_palindrome(self):
        self.assertTrue(palindrome("a"))
        self.assertTrue(palindrome("aa"))
        self.assertTrue(palindrome("aba"))
        self.assertTrue(palindrome("abba"))

        self.assertFalse(palindrome("abc"))
        self.assertFalse(palindrome("ab"))