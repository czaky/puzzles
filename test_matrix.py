"""Test module for the matrix related puzzles."""

from itertools import islice
import unittest
import matrix as m


def parse(n: int, k: int, s: str):
    "Parse a matrix `n x k` from string `s`."
    nums = map(int, s.split())
    return [list(islice(nums, k)) for i in range(n)]


class TestMatrixPuzzles(unittest.TestCase):
    """Test class for the matrix related puzzles."""

    def test_find_sorted(self):
        "Test `find_sorted` function."
        self.assertTrue(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 52))
        self.assertTrue(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 38))
        self.assertTrue(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 57))
        self.assertTrue(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 69))
        self.assertTrue(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 3))
        self.assertFalse(m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 62))

    def test_optimum_multiplications(self):
        "Test `optimum_multiplications`."
        self.assertEqual(580, m.optimum_multiplications([2, 40, 2, 40, 5]))
        self.assertEqual(26000, m.optimum_multiplications([40, 20, 30, 10, 30]))

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
        self.assertTrue(m.sudoku(grid))
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

    def test_fib(self):
        "Test `fib."
        self.assertEqual(1, m.fib(0, 5))
        self.assertEqual(1, m.fib(2, 5))
        self.assertEqual(1, m.fib(1, 5))
        self.assertEqual(2, m.fib(3, 5))
        self.assertEqual(3, m.fib(4, 5))
        self.assertEqual(0, m.fib(5, 5))
        self.assertEqual(3, m.fib(6, 5))

    def test_generic_fib(self):
        "Test `generic_fib."
        self.assertEqual(4, m.generic_fib(3, 3, 3, 3, 5))

    def test_max_sum_rectangle(self):
        "Test `max_sum_rectangle`."
        self.assertEqual(3, m.max_sum_rectangle([[1, 2]]))
        self.assertEqual(4, m.max_sum_rectangle([[1], [3]]))
        self.assertEqual(10, m.max_sum_rectangle([[1, 2], [3, 4]]))
        self.assertEqual(-1, m.max_sum_rectangle([[-1, -2], [-3, -4]]))
        self.assertEqual(
            29,
            m.max_sum_rectangle(
                [
                    [1, 2, -1, -4, -20],
                    [-8, -3, 4, 2, 1],
                    [3, 8, 10, 1, 3],
                    [-4, -1, 1, 7, -6],
                ]
            ),
        )
        self.assertEqual(
            16,
            m.max_sum_rectangle(
                [
                    [9, -9, 1, -4, -1, 9, -10],
                    [3, -3, -4, -2, -5, 3, -6],
                    [-7, 2, -5, 1, -10, 4, -4],
                ]
            ),
        )

    def test_zero_sum_sub_matrix(self):
        "Test `zero_sum_sub_matrix`."
        self.assertEqual(
            [[1, 2, 3], [-3, -2, -1]],
            m.zero_sum_sub_matrix([[1, 2, 3], [-3, -2, -1], [1, 7, 5]]),
        )
        self.assertEqual(
            [[-6, -7], [8, 7], [-2, 0]],
            m.zero_sum_sub_matrix(
                [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]]
            ),
        )
        mat = m.make(
            """\
            -4 6 6
            1 7 8
            0 -11 -6
            4 5 -1
            10 -6 -7
            -9 -7 0
            -7 1 -2
            -9 7 -2
            -6 -2 -8
            5 5 0
            1 0 6
            3 1 6
            -2 -6 -7
            -9 4 5
            7 -1 -3
            -2 -7 -11
            8 -11 -3
            -5 -4 10
            1 4 7"""
        )
        self.assertEqual(
            [[-6, -2], [5, 5], [1, 0], [3, 1], [-2, -6], [-9, 4], [7, -1]],
            m.zero_sum_sub_matrix(mat),
        )
