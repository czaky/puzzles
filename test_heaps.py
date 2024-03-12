"""Test module for the heap related puzzles."""

import unittest
import heaps as h


class TestHeaps(unittest.TestCase):
    """Test class for the heap related puzzles."""

    def test_connect_ropes_cost(self):
        "Test the `connect_ropes_cost` function."
        self.assertEqual(0, h.connect_ropes_cost([1]))
        self.assertEqual(5, h.connect_ropes_cost([2, 3]))
        self.assertEqual(29, h.connect_ropes_cost([4, 3, 2, 6]))
