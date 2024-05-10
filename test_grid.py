"""Test module for the search."""

import unittest
from typing import Callable

import grid as g
from grid import parse


class TestGrid(unittest.TestCase):
    """Test class for the grid based puzzles."""

    def test_dijkstra(self):
        """Test the `dijkstra` search function."""
        assert g.dijkstra([[4, 4], [3, 7]]) == 14
        assert (
            g.dijkstra([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]) == 43
        )
        assert (
            g.dijkstra(
                [
                    [9, 4, 900, 900],
                    [600, 7, 600, 400],
                    [800, 3, 3, 700],
                    [700, 400, 9, 10],
                ],
            )
            == 45
        )

    def test_a_star(self):
        """Test the `a_star_grid` search function."""
        assert g.a_star([[4, 4], [3, 7]]) == 14
        assert g.a_star([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]) == 43
        assert (
            g.a_star(
                [
                    [9, 4, 900, 900],
                    [600, 7, 600, 400],
                    [800, 3, 3, 700],
                    [700, 400, 9, 10],
                ],
            )
            == 45
        )

    def test_connect_islands(self):
        """Test `connect_islands`."""
        assert g.connect_islands([[0, 0], [0, 0]]) == 1
        assert g.connect_islands([[0, 0], [0, 1]]) == 2
        assert g.connect_islands([[1, 0], [0, 1]]) == 3
        assert g.connect_islands([[1, 0], [1, 1]]) == 4
        assert g.connect_islands([[1, 1], [1, 1]]) == 4

        m = parse("""\
        1 1 1 0 1 0
        1 0 1 0 0 0
        0 0 1 1 0 1
        1 1 0 0 0 0
        0 0 1 1 1 0
        1 0 1 1 0 0""")

        assert g.connect_islands(m) == 15

    def test_enclosed_islands_count(self):
        """Test `enclosed_islands_count`."""
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
        ]
        assert g.enclosed_islands_count(grid) == 2

    def test_sudoku(self):
        """Test `sudoku` puzzle solver."""
        grid = parse(
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
        assert g.sudoku(grid)
        assert [
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9],
        ] == grid

    def test_grid_path_count(self):
        """Test `grid_path_count`."""
        assert g.grid_path_count(3, 0) == 1
        assert g.grid_path_count(3, 6) == 84
        assert g.grid_path_count(6, 3) == 84
        assert g.grid_path_count(6, 6) == 924
        assert g.grid_path_count(35, 31) == 21144547

    def test_min_points_traverse(self):
        """Test `min_points_traverse`."""
        assert g.min_points_traverse([[]]) == 1
        assert g.min_points_traverse([[1]]) == 1
        assert g.min_points_traverse([[0]]) == 1
        assert g.min_points_traverse([[-1]]) == 2
        assert g.min_points_traverse([[-5]]) == 6
        assert g.min_points_traverse([[1, 2, 3]]) == 1
        assert g.min_points_traverse([[1, 2, 3], [4, 5, 6]]) == 1
        assert g.min_points_traverse([[-5, 2, 3], [4, 5, 6]]) == 6
        assert g.min_points_traverse([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7

    def test_grid_exit(self):
        """Test `grid_exit`."""
        assert g.grid_exit([[0]]) == (0, 0)
        assert g.grid_exit([[0, 1, 0]]) == (0, 1)
        assert g.grid_exit([[0, 1, 0], [0, 1, 1], [0, 0, 0]]) == (1, 0)

    def _test_shortest_path_with_walls(self, shortest_path: Callable) -> None:
        """Test `shortest_path_with_walls`."""
        gr = [
            [0, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 0],
        ]
        assert shortest_path(gr, 2) == 8
        gr = g.parse(
            """\
            0 0 1
            1 0 0
            0 0 0
            0 0 0
            1 1 0
            0 0 0
            0 0 0
            0 1 0
            0 0 0
            0 0 1
            0 0 0
            0 0 0
            1 0 0
            0 0 0
            0 0 0
            0 0 0
            0 0 1
            1 0 0
            0 0 0
            0 0 0
            0 0 0
            0 0 0
            0 0 0
            0 0 0
            1 0 0
            0 0 1
            0 0 0
            0 0 0
            0 0 1
            0 1 0
            1 0 0
            0 0 0
            0 0 0""",
        )
        assert shortest_path(gr, 4) == 34
        gr = g.parse(
            """
            0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 0
            0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1
            0 0 1 0 1 0 0 1 0 0 0 0 0 0 1 0 1
            0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0
            0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1
            0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
            1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0
            0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0
            0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0
            0 0 0 0 0 1 0 0 0 1 0 0 1 1 0 0 0
            0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
            0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0
            0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
            0 0 1 0 0 0 0 0 1 1 0 0 0 1 1 1 0
            0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
            0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
            0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 1 0
            0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0
            0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
            0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
            1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
            0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0
            0 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1
            0 1 1 0 0 1 0 1 0 0 1 1 0 0 0 0 0
            0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0""",
        )

        assert shortest_path(gr, 0) == 45

    def test_shortest_path_with_walls_heap(self):
        """Test `shortest_path_with_walls (heap)."""
        self._test_shortest_path_with_walls(g.shortest_path_with_walls_heap)

    def test_shortest_path_with_walls_bfs(self):
        """Test `shortest_path_with_walls (bfs)."""
        self._test_shortest_path_with_walls(g.shortest_path_with_walls_bfs)
