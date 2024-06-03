"""Test module for the matrix related puzzles."""

import unittest
from itertools import islice

import matrix as m


def parse(n: int, k: int, s: str):
    """Parse a matrix `n x k` from string `s`."""
    nums = map(int, s.split())
    return [list(islice(nums, k)) for i in range(n)]


class TestMatrixPuzzles(unittest.TestCase):
    """Test class for the matrix related puzzles."""

    def test_find_sorted(self):
        """Test `find_sorted` function."""
        assert m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 52)
        assert m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 38)
        assert m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 57)
        assert m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 69)
        assert m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 3)
        assert not m.find_sorted([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 62)

    def test_optimum_multiplications(self):
        """Test `optimum_multiplications`."""
        assert m.optimum_multiplications([2, 40, 2, 40, 5]) == 580
        assert m.optimum_multiplications([40, 20, 30, 10, 30]) == 26000

    def test_balloon_coin_popping(self):
        assert m.balloon_coin_popping([]) == 0
        assert m.balloon_coin_popping([5]) == 5
        assert m.balloon_coin_popping([5, 10]) == 60
        assert m.balloon_coin_popping([3, 1, 5, 8]) == 167

    def test_optimum_brackets(self):
        """Test `optimum_brackets`."""
        assert m.optimum_brackets([3, 3]) == "A"
        assert m.optimum_brackets([3, 3, 3]) == "AB"
        assert m.optimum_brackets([1, 2, 3, 4, 5]) == "ABCD"
        assert m.optimum_brackets([5, 4, 3, 2, 1]) == "A(B(CD))"
        assert m.optimum_brackets([4, 2, 3, 1, 3]) == "A(BC)D"

    def test_max_sum_rectangle(self):
        """Test `max_sum_rectangle`."""
        assert m.max_sum_rectangle([[1, 2]]) == 3
        assert m.max_sum_rectangle([[1], [3]]) == 4
        assert m.max_sum_rectangle([[1, 2], [3, 4]]) == 10
        assert m.max_sum_rectangle([[-1, -2], [-3, -4]]) == -1
        assert (
            m.max_sum_rectangle(
                [
                    [1, 2, -1, -4, -20],
                    [-8, -3, 4, 2, 1],
                    [3, 8, 10, 1, 3],
                    [-4, -1, 1, 7, -6],
                ],
            )
            == 29
        )
        assert (
            m.max_sum_rectangle(
                [
                    [9, -9, 1, -4, -1, 9, -10],
                    [3, -3, -4, -2, -5, 3, -6],
                    [-7, 2, -5, 1, -10, 4, -4],
                ],
            )
            == 16
        )

    def test_zero_sum_sub_matrix(self):
        """Test `zero_sum_sub_matrix`."""
        assert [[1, 2, 3], [-3, -2, -1]] == m.zero_sum_sub_matrix(
            [[1, 2, 3], [-3, -2, -1], [1, 7, 5]],
        )
        assert [[-6, -7], [8, 7], [-2, 0]] == m.zero_sum_sub_matrix(
            [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]],
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
            1 4 7""",
        )
        assert [
            [-6, -2],
            [5, 5],
            [1, 0],
            [3, 1],
            [-2, -6],
            [-9, 4],
            [7, -1],
        ] == m.zero_sum_sub_matrix(mat)
