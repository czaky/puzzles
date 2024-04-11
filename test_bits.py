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

    def test_max_xor_sub_array(self):
        "Test `max_xor_sub_array`."
        self.assertEqual(0, b.max_xor_sub_array([])[0])
        self.assertEqual([], b.max_xor_sub_array([])[1])
        self.assertEqual(1, b.max_xor_sub_array([1])[0])
        self.assertEqual([1], b.max_xor_sub_array([1])[1])

        self.assertEqual(3, b.max_xor_sub_array([1, 2])[0])
        self.assertEqual([1, 2], b.max_xor_sub_array([1, 2])[1])
        self.assertEqual(3, b.max_xor_sub_array([2, 1])[0])
        self.assertEqual([2, 1], b.max_xor_sub_array([2, 1])[1])

        self.assertEqual(3, b.max_xor_sub_array([1, 3])[0])
        self.assertEqual([3], b.max_xor_sub_array([1, 3])[1])
        self.assertEqual(3, b.max_xor_sub_array([3, 1])[0])
        self.assertEqual([3], b.max_xor_sub_array([3, 1])[1])

        self.assertEqual(7, b.max_xor_sub_array([1, 2, 3, 4, 5])[0])
        self.assertEqual([3, 4], b.max_xor_sub_array([1, 2, 3, 4, 5])[1])
        self.assertEqual(13, b.max_xor_sub_array([1, 2, 3, 4, 5, 8])[0])
        self.assertEqual([5, 8], b.max_xor_sub_array([1, 2, 3, 4, 5, 8])[1])

        self.assertEqual(7, b.max_xor_sub_array([5, 4, 3, 2, 1])[0])
        self.assertEqual([4, 3], b.max_xor_sub_array([5, 4, 3, 2, 1])[1])
        self.assertEqual(13, b.max_xor_sub_array([8, 5, 4, 3, 2, 1])[0])
        self.assertEqual([8, 5], b.max_xor_sub_array([8, 5, 4, 3, 2, 1])[1])
