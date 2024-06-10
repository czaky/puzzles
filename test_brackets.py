"""Test module for the brackets puzzles."""

import unittest

import brackets as b


class TestBrackets(unittest.TestCase):
    """Test class for brackets module."""

    def test_balanced(self):
        """Tests `balanced` function."""
        assert b.balanced("({[()[]]})")
        assert b.balanced("{}[]()")
        assert not b.balanced("{}[]()[")
        assert not b.balanced("){}[]()")
        assert not b.balanced("{)[]()")

    def test_longest_balanced_parenthesis_substring(self):
        assert b.longest_balanced_parenthesis_substring("(()(") == 2
        assert b.longest_balanced_parenthesis_substring("()(())(") == 6
