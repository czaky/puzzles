"""Test for utilities from 'sequences.py`."""

import unittest

import sequences as s


class TestSequences(unittest.TestCase):
    """Test class for the utils operating on sequences."""

    def test_at(self):
        """Test `at`."""
        assert [4, 5, 6] == s.at(1)([[1, 2, 3], [4, 5, 6]])
        assert s.at(1, 2)([[1, 2, 3], [4, 5, 6]]) == 6
        assert [[1, 2, 3], [4, 5, 6]] == s.at()([[1, 2, 3], [4, 5, 6]])
