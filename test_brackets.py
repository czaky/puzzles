"""Test module for the brackets puzzles."""

import unittest

import brackets as b


class TestBrackets(unittest.TestCase):
    """Test class for brackets module."""

    def test_balanced(self):
        """Tests `balanced` function."""
        self.assertTrue(b.balanced("({[()[]]})"))
        self.assertTrue(b.balanced("{}[]()"))
        self.assertFalse(b.balanced("{}[]()["))
        self.assertFalse(b.balanced("){}[]()"))
        self.assertFalse(b.balanced("{)[]()"))
