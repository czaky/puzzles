"""Test module for the search."""

import unittest
from itertools import islice

import grid as g


def parse(n: int, k: int, s: str):
    "Parse a matrix `n x k` from string `s`."
    nums = map(int, s.split())
    return [list(islice(nums, k)) for i in range(n)]


class TestGrid(unittest.TestCase):
    """Test class for the grid based puzzles."""

    def test_dijkstra(self):
        "Test the `dijkstra` search function."
        self.assertEqual(14, g.dijkstra([[4, 4], [3, 7]]))
        self.assertEqual(
            43,
            g.dijkstra([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]),
        )
        self.assertEqual(
            45,
            g.dijkstra(
                [
                    [9, 4, 900, 900],
                    [600, 7, 600, 400],
                    [800, 3, 3, 700],
                    [700, 400, 9, 10],
                ]
            ),
        )

    def test_a_star(self):
        "Test the `a_star_grid` search function."
        self.assertEqual(14, g.a_star([[4, 4], [3, 7]]))
        self.assertEqual(
            43, g.a_star([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]])
        )
        self.assertEqual(
            45,
            g.a_star(
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
        self.assertEqual(1, g.connect_islands([[0, 0], [0, 0]]))
        self.assertEqual(2, g.connect_islands([[0, 0], [0, 1]]))
        self.assertEqual(3, g.connect_islands([[1, 0], [0, 1]]))
        self.assertEqual(4, g.connect_islands([[1, 0], [1, 1]]))
        self.assertEqual(4, g.connect_islands([[1, 1], [1, 1]]))

        mat = """\
        1 1 1 0 1 0
        1 0 1 0 0 0
        0 0 1 1 0 1
        1 1 0 0 0 0
        0 0 1 1 1 0
        1 0 1 1 0 0"""

        m = [list(map(int, l.split())) for l in mat.splitlines()]

        self.assertEqual(15, g.connect_islands(m))

    def test_enclosed_islands_count(self):
        "Test `enclosed_islands_count`."
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
        ]
        self.assertEqual(2, g.enclosed_islands_count(grid))

    def test_sudoku(self):
        "Test `sudoku` puzzle solver."
        grid = parse(
            9,
            9,
            """
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0""",
        )
        self.assertTrue(g.sudoku(grid))
        self.assertEqual(
            [
                [3, 1, 6, 5, 7, 8, 4, 9, 2],
                [5, 2, 9, 1, 3, 4, 7, 6, 8],
                [4, 8, 7, 6, 2, 9, 5, 3, 1],
                [2, 6, 3, 4, 1, 5, 9, 8, 7],
                [9, 7, 4, 8, 6, 3, 1, 2, 5],
                [8, 5, 1, 7, 9, 2, 6, 4, 3],
                [1, 3, 8, 9, 4, 7, 2, 5, 6],
                [6, 9, 2, 3, 5, 1, 8, 7, 4],
                [7, 4, 5, 2, 8, 6, 3, 1, 9],
            ],
            grid,
        )

    def test_grid_path_count(self):
        "Test `grid_path_count`."
        self.assertEqual(1, g.grid_path_count(3, 0))
        self.assertEqual(84, g.grid_path_count(3, 6))
        self.assertEqual(84, g.grid_path_count(6, 3))
        self.assertEqual(924, g.grid_path_count(6, 6))
        self.assertEqual(21144547, g.grid_path_count(35, 31))

    def test_min_points_traverse(self):
        "Test `min_points_traverse`."
        self.assertEqual(1, g.min_points_traverse([[]]))
        self.assertEqual(1, g.min_points_traverse([[1]]))
        self.assertEqual(1, g.min_points_traverse([[0]]))
        self.assertEqual(2, g.min_points_traverse([[-1]]))
        self.assertEqual(6, g.min_points_traverse([[-5]]))
        self.assertEqual(1, g.min_points_traverse([[1, 2, 3]]))
        self.assertEqual(1, g.min_points_traverse([[1, 2, 3], [4, 5, 6]]))
        self.assertEqual(6, g.min_points_traverse([[-5, 2, 3], [4, 5, 6]]))
        self.assertEqual(
            7, g.min_points_traverse([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        )

    def test_grid_exit(self):
        "Test `grid_exit`."
        self.assertEqual((0, 0), g.grid_exit([[0]]))
        self.assertEqual((0, 1), g.grid_exit([[0, 1, 0]]))
        self.assertEqual((1, 0), g.grid_exit([[0, 1, 0], [0, 1, 1], [0, 0, 0]]))
