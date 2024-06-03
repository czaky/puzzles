"""Test module for the graph based puzzles."""

import unittest

import sets as s


class TestSets(unittest.TestCase):
    """Test class for the set based puzzles."""

    def test_weighted_paths_in_tree(self):
        """Test `weighted_paths_in_tree`."""
        assert [1] == s.weighted_paths_in_tree([[1, 2, 1], [2, 3, 4]], [3])
        assert [1, 3, 4] == s.weighted_paths_in_tree(
            [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]],
            [1, 3, 5],
        )
        assert [6, 6, 3, 0, 3, 0, 6, 0, 6] == s.weighted_paths_in_tree(
            [(3, 1, 3), (4, 2, 2), (3, 4, 1)],
            [3, 3, 2, 0, 2, 0, 3, 0, 3],
        )

    def test_powerset(self):
        """Test `powerset`."""
        assert [set(), {0}, {1}, {2}, {0, 1}, {0, 2}, {1, 2}, {0, 1, 2}] == list(
            s.powerset(range(3)),
        )

    def test_merge_email_accounts(self):
        assert s.merge_email_accounts(
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        ) == [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"],
        ]

        assert s.merge_email_accounts(
            [
                ["Gabe", "Gabe00@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
            ]
        ) == [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
            ["Gabe", "Gabe00@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
        ]
