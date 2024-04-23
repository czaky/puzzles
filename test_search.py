"""Test module for the search."""

import unittest

import search as s


class TestSearch(unittest.TestCase):
    """Test class for the search puzzles."""

    def test_dijkstra_grid(self):
        "Test the `dijkstra` search function."
        self.assertEqual(14, s.dijkstra_grid([[4, 4], [3, 7]]))
        self.assertEqual(
            43,
            s.dijkstra_grid([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]),
        )
        self.assertEqual(
            45,
            s.dijkstra_grid(
                [
                    [9, 4, 900, 900],
                    [600, 7, 600, 400],
                    [800, 3, 3, 700],
                    [700, 400, 9, 10],
                ]
            ),
        )

    def test_a_star_grid(self):
        "Test the `a_star_grid` search function."
        self.assertEqual(14, s.a_star_grid([[4, 4], [3, 7]]))
        self.assertEqual(
            43, s.a_star_grid([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]])
        )
        self.assertEqual(
            45,
            s.a_star_grid(
                [
                    [9, 4, 900, 900],
                    [600, 7, 600, 400],
                    [800, 3, 3, 700],
                    [700, 400, 9, 10],
                ]
            ),
        )

    def test_connect_islands(self):
        "Test `connect_islands`."
        self.assertEqual(1, s.connect_islands([[0, 0], [0, 0]]))
        self.assertEqual(2, s.connect_islands([[0, 0], [0, 1]]))
        self.assertEqual(3, s.connect_islands([[1, 0], [0, 1]]))
        self.assertEqual(4, s.connect_islands([[1, 0], [1, 1]]))
        self.assertEqual(4, s.connect_islands([[1, 1], [1, 1]]))

        mat = """\
        1 1 1 0 1 0
        1 0 1 0 0 0
        0 0 1 1 0 1
        1 1 0 0 0 0
        0 0 1 1 1 0
        1 0 1 1 0 0"""

        m = [list(map(int, l.split())) for l in mat.splitlines()]

        self.assertEqual(15, s.connect_islands(m))

    def test_enclosed_islands_count(self):
        "Test `enclosed_islands_count`."
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
        ]
        self.assertEqual(2, s.enclosed_islands_count(grid))

    def test_largest_sum_cycle(self):
        "Test `largest_sum_cycle`."
        self.assertEqual(3, s.largest_sum_cycle([2, 2, 1, 2, 2]))
        self.assertEqual(3, s.largest_sum_cycle([1, 2, 0, -1]))
        self.assertEqual(3, s.largest_sum_cycle([1, 2, 1]))
        self.assertEqual(-1, s.largest_sum_cycle([2, 0, -1, 2]))
        e = [7, 3, -1, 1, 9, 0, 3, 5, 5, 3]
        self.assertEqual(12, s.largest_sum_cycle(e))
