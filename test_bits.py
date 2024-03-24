"""Test module for the bits based puzzles."""

import unittest
import bits as b


class TestBits(unittest.TestCase):
    """Test class for the bits based puzzles."""

    def test_count_different_bit_pairs(self):
        "Test `count_different_bit_pairs`."
        self.assertEqual(2, b.count_different_bit_pairs([1, 3]))
        self.assertEqual(4, b.count_different_bit_pairs([2, 4]))
        self.assertEqual(8, b.count_different_bit_pairs([1, 3, 5]))
