"""Test module for the bits based puzzles."""

import unittest

import bits as b


class TestBits(unittest.TestCase):
    """Test class for the bits based puzzles."""

    def test_count_different_bit_pairs(self):
        """Test `count_different_bit_pairs`."""
        assert b.count_different_bit_pairs([1, 3]) == 2
        assert b.count_different_bit_pairs([2, 4]) == 4
        assert b.count_different_bit_pairs([1, 3, 5]) == 8

    def test_max_xor_sub_array(self):
        """Test `max_xor_sub_array`."""
        assert b.max_xor_sub_array([])[0] == 0
        assert [] == b.max_xor_sub_array([])[1]
        assert b.max_xor_sub_array([1])[0] == 1
        assert [1] == b.max_xor_sub_array([1])[1]

        assert b.max_xor_sub_array([1, 2])[0] == 3
        assert [1, 2] == b.max_xor_sub_array([1, 2])[1]
        assert b.max_xor_sub_array([2, 1])[0] == 3
        assert [2, 1] == b.max_xor_sub_array([2, 1])[1]

        assert b.max_xor_sub_array([1, 3])[0] == 3
        assert [3] == b.max_xor_sub_array([1, 3])[1]
        assert b.max_xor_sub_array([3, 1])[0] == 3
        assert [3] == b.max_xor_sub_array([3, 1])[1]

        assert b.max_xor_sub_array([1, 2, 3, 4, 5])[0] == 7
        assert [3, 4] == b.max_xor_sub_array([1, 2, 3, 4, 5])[1]
        assert b.max_xor_sub_array([1, 2, 3, 4, 5, 8])[0] == 13
        assert [5, 8] == b.max_xor_sub_array([1, 2, 3, 4, 5, 8])[1]

        assert b.max_xor_sub_array([5, 4, 3, 2, 1])[0] == 7
        assert [4, 3] == b.max_xor_sub_array([5, 4, 3, 2, 1])[1]
        assert b.max_xor_sub_array([8, 5, 4, 3, 2, 1])[0] == 13
        assert [8, 5] == b.max_xor_sub_array([8, 5, 4, 3, 2, 1])[1]

    def test_max_xor_subset(self):
        """Test `max_xor_aubset`."""
        assert b.max_xor_subset([]) == 0
        assert b.max_xor_subset([1]) == 1

        assert b.max_xor_subset([1, 2]) == 3
        assert b.max_xor_subset([2, 1]) == 3

        assert b.max_xor_subset([1, 3]) == 3
        assert b.max_xor_subset([3, 1]) == 3

        assert b.max_xor_subset([1, 2, 3, 4, 5]) == 7
        assert b.max_xor_subset([1, 2, 3, 4, 5, 8]) == 15

        assert b.max_xor_subset([5, 4, 3, 2, 1]) == 7
        assert b.max_xor_subset([8, 5, 4, 3, 2, 1]) == 15

        assert b.max_xor_subset([9, 8, 5]) == 13
        assert b.max_xor_subset([96, 51, 26, 52]) == 125
        assert b.max_xor_subset([1, 2, 3, 4, 5, 6, 22, 33, 44, 22, 111]) == 127
