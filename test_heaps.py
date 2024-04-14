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

    def test_smallest_intersecting_rage(self):
        "Test `smallest_intersecting_range`."
        self.assertEqual((1, 1), h.smallest_intersecting_range([[1]]))
        self.assertEqual(
            (5, 8),
            h.smallest_intersecting_range(
                [[1, 3, 5], [7, 8, 9], [2, 4, 6], [2, 3, 8], [5, 7, 11]]
            ),
        )
        self.assertEqual(
            (501, 511),
            h.smallest_intersecting_range(
                [
                    [10, 30, 500, 501],
                    [70, 80, 509, 510],
                    [20, 40, 506, 507],
                    [20, 30, 508, 509],
                    [50, 70, 511, 512],
                ]
            ),
        )
        self.assertEqual(
            (1, 2),
            h.smallest_intersecting_range(
                [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]]
            ),
        )
