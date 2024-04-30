"""Test module for the graph based puzzles."""

import unittest

import graphs as g


class TestGraphs(unittest.TestCase):
    """Test class for the graph based puzzles."""

    def test_breadth_first(self):
        "Test `breadth_first` traversal."
        adj = [[1, 2, 3], [], [4], [], []]
        self.assertEqual([0, 1, 2, 3, 4], g.breadth_first(adj))

    def test_depth_first(self):
        "Test `depth_first` traversal."
        adj = [[1, 2, 3], [], [4], [], []]
        self.assertEqual([0, 1, 2, 4, 3], g.depth_first(adj))

    def test_circle_of_words(self):
        "Test `circle_of_words`."
        self.assertTrue(g.circle_of_words(["abc", "cde", "eda"]))
        self.assertFalse(g.circle_of_words(["abc", "cde", "edf"]))

    def test_articulation_points(self):
        "Test `articulation_points`."
        adj = [[1, 2], [0], [0]]
        self.assertEqual([0], g.articulation_points(adj))
        adj = [[1, 2], [0, 2], [0, 1, 3], [2]]
        self.assertEqual([2], g.articulation_points(adj))
        adj = [[1], [2, 0], [1, 3, 4], [2, 4], [2, 3]]
        self.assertEqual([1, 2], g.articulation_points(adj))
        adj = [[1], [0, 4], [3, 4], [2, 4], [1, 2, 3]]
        self.assertEqual([1, 4], g.articulation_points(adj))
        adj = [
            [1],
            [0, 2, 5],
            [1, 3, 6, 7],
            [2, 4, 5],
            [3, 5],
            [4, 1, 3],
            [2, 7],
            [6, 2],
        ]
        self.assertEqual([1, 2], g.articulation_points(adj))
        adj = [
            [6, 5, 4],
            [8, 5],
            [6, 7],
            [5],
            [8, 0],
            [0, 3, 1],
            [0, 8, 7, 2],
            [6, 2],
            [6, 4, 1],
        ]
        self.assertEqual([5, 6], g.articulation_points(adj))
        adj = [
            [1, 2, 3, 6, 8],
            [0, 2, 3, 4, 5, 6],
            [0, 1, 3, 6, 8],
            [0, 1, 2, 4, 6, 8],
            [1, 3, 8],
            [1, 6],
            [0, 1, 2, 3, 5, 7, 8],
            [6],
            [0, 2, 3, 4, 6],
        ]
        self.assertEqual([6], g.articulation_points(adj))
        adj = [
            [8, 2, 5, 6],
            [8],
            [0, 6],
            [8, 9],
            [8],
            [0, 7],
            [0, 9, 2],
            [5],
            [0, 1, 3, 4],
            [3, 6],
        ]
        self.assertEqual([0, 5, 8], g.articulation_points(adj))
        adj = [
            [2, 2, 1, 3, 6, 8],
            [3, 4, 2, 5, 5, 3, 0, 6],
            [1, 2, 2, 0, 6, 6, 2, 2, 0, 6, 8, 3],
            [4, 1, 6, 8, 1, 0, 4, 2],
            [3, 1, 8, 3],
            [5, 5, 1, 6, 1, 6],
            [6, 6, 2, 2, 3, 6, 6, 5, 2, 8, 1, 5, 0, 7],
            [6],
            [3, 2, 6, 4, 0],
        ]
        self.assertEqual([6], g.articulation_points(adj))
        adj = [[5, 4], [3], [5], [1, 4], [6, 0, 3], [0, 2], [4]]
        self.assertEqual([0, 3, 4, 5], g.articulation_points(adj))
        adj = [[1], [0, 4], [4, 3], [4, 2], [1, 2, 3]]
        self.assertEqual([1, 4], g.articulation_points(adj))

    def test_articulation_points_recursive(self):
        "Test `articulation_points_recursive`."
        adj = [[1, 2], [0], [0]]
        self.assertEqual([0], g.articulation_points_recursive(adj))
        adj = [[1, 2], [0, 2], [0, 1, 3], [2]]
        self.assertEqual([2], g.articulation_points_recursive(adj))
        adj = [[1], [2, 0], [1, 3, 4], [2, 4], [2, 3]]
        self.assertEqual([1, 2], g.articulation_points_recursive(adj))
        adj = [[1], [0, 4], [3, 4], [2, 4], [1, 2, 3]]
        self.assertEqual([1, 4], g.articulation_points_recursive(adj))
        adj = [
            [1],
            [0, 2, 5],
            [1, 3, 6, 7],
            [2, 4, 5],
            [3, 5],
            [4, 1, 3],
            [2, 7],
            [6, 2],
        ]
        self.assertEqual([1, 2], g.articulation_points_recursive(adj))
        adj = [
            [6, 5, 4],
            [8, 5],
            [6, 7],
            [5],
            [8, 0],
            [0, 3, 1],
            [0, 8, 7, 2],
            [6, 2],
            [6, 4, 1],
        ]
        self.assertEqual([5, 6], g.articulation_points_recursive(adj))
        adj = [
            [1, 2, 3, 6, 8],
            [0, 2, 3, 4, 5, 6],
            [0, 1, 3, 6, 8],
            [0, 1, 2, 4, 6, 8],
            [1, 3, 8],
            [1, 6],
            [0, 1, 2, 3, 5, 7, 8],
            [6],
            [0, 2, 3, 4, 6],
        ]
        self.assertEqual([6], g.articulation_points_recursive(adj))
        adj = [
            [8, 2, 5, 6],
            [8],
            [0, 6],
            [8, 9],
            [8],
            [0, 7],
            [0, 9, 2],
            [5],
            [0, 1, 3, 4],
            [3, 6],
        ]
        self.assertEqual([0, 5, 8], g.articulation_points_recursive(adj))
        adj = [
            [2, 2, 1, 3, 6, 8],
            [3, 4, 2, 5, 5, 3, 0, 6],
            [1, 2, 2, 0, 6, 6, 2, 2, 0, 6, 8, 3],
            [4, 1, 6, 8, 1, 0, 4, 2],
            [3, 1, 8, 3],
            [5, 5, 1, 6, 1, 6],
            [6, 6, 2, 2, 3, 6, 6, 5, 2, 8, 1, 5, 0, 7],
            [6],
            [3, 2, 6, 4, 0],
        ]
        self.assertEqual([6], g.articulation_points_recursive(adj))
        adj = [[5, 4], [3], [5], [1, 4], [6, 0, 3], [0, 2], [4]]
        self.assertEqual([0, 3, 4, 5], g.articulation_points_recursive(adj))
        adj = [[1], [0, 4], [4, 3], [4, 2], [1, 2, 3]]
        self.assertEqual([1, 4], g.articulation_points_recursive(adj))

    def test_critical_connections(self):
        "Test `critical_connections`."
        adj = [[1, 2], [0], [0]]
        self.assertEqual([(0, 1), (0, 2)], g.critical_connections(adj))
        adj = [[1], [2, 0], [1, 4, 3], [2, 4], [3, 2]]
        self.assertEqual([(0, 1), (1, 2)], g.critical_connections(adj))
        adj = [[1, 2], [0, 2], [0, 1, 3], [2]]
        self.assertEqual([(2, 3)], g.critical_connections(adj))
        adj = [
            [6, 5, 4],
            [8, 5],
            [6, 7],
            [5],
            [8, 0],
            [0, 3, 1],
            [0, 8, 7, 2],
            [6, 2],
            [6, 4, 1],
        ]
        self.assertEqual([(3, 5)], g.critical_connections(adj))

    def test_strongly_connected_components(self):
        "Test `strongly_connected_components`."
        adj = [[1], [2, 3], [0], [4], [5], [3]]
        scc = [[0, 1, 2], [3, 4, 5]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[1], [2, 4], [3], [1], [0]]
        scc = [[0, 1, 2, 3, 4]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]]
        scc = [[0, 1, 2, 3]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[2, 3], [0], [1], [4], []]
        scc = [[0, 1, 2], [3], [4]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[], [3], [1], [9, 0, 8], [5], [4, 3], [6], [3], [5, 6], [5, 9]]
        scc = [[0], [1], [2], [3, 4, 5, 8, 9], [6], [7]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[9, 3, 8], [0], [1], [], [5], [4, 0], [6], [0], [5, 6], [5, 9]]
        scc = [[0, 4, 5, 8, 9], [1], [2], [3], [6], [7]]
        self.assertEqual(scc, g.strongly_connected_components(adj))
        adj = [[2], [4, 7, 0], [], [1, 7, 3], [4, 3], [], [3, 5], [6]]
        scc = [[0], [1, 3, 4, 6, 7], [2], [5]]
        self.assertEqual(scc, g.strongly_connected_components(adj))

    def test_strongly_connected_components_recursive(self):
        "Test `strongly_connected_components_recursive`."
        adj = [[1], [2, 3], [0], [4], [5], [3]]
        scc = [[0, 1, 2], [3, 4, 5]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[1], [2, 4], [3], [1], [0]]
        scc = [[0, 1, 2, 3, 4]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]]
        scc = [[0, 1, 2, 3]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[2, 3], [0], [1], [4], []]
        scc = [[0, 1, 2], [3], [4]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[], [3], [1], [9, 0, 8], [5], [4, 3], [6], [3], [5, 6], [5, 9]]
        scc = [[0], [1], [2], [3, 4, 5, 8, 9], [6], [7]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[9, 3, 8], [0], [1], [], [5], [4, 0], [6], [0], [5, 6], [5, 9]]
        scc = [[0, 4, 5, 8, 9], [1], [2], [3], [6], [7]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))
        adj = [[2], [4, 7, 0], [], [1, 7, 3], [4, 3], [], [3, 5], [6]]
        scc = [[0], [1, 3, 4, 6, 7], [2], [5]]
        self.assertEqual(scc, g.strongly_connected_components_recursive(adj))

    def test_vertex_cover_optimal(self):
        "Test `vertex_cover_optimal`."
        self.assertEqual({1}, g.vertex_cover_optimal([[1, 2]]))
        self.assertEqual(
            {1, 2, 3},
            g.vertex_cover_optimal([[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]),
        )

    def test_word_distance(self):
        "Test `word_distance`."
        self.assertEqual(1, g.word_distance([], "foo", "foo"))
        self.assertEqual(0, g.word_distance([], "foo", "bar"))

        self.assertEqual(2, g.word_distance(["foo", "baz", "qux"], "bar", "baz"))
        self.assertEqual(
            3, g.word_distance(["des", "der", "dfr", "dgt", "dfs"], "der", "dfs")
        )
        self.assertEqual(
            3, g.word_distance(["des", "der", "dfr", "dgt", "dfs"], "dep", "dfs")
        )
        self.assertEqual(4, g.word_distance(WORDS, "lkljl", "ljkll"))

    def test_word_paths(self):
        "Test `word_paths`."
        self.assertEqual([["foo"]], g.word_paths([], "foo", "foo"))
        self.assertEqual([], g.word_paths([], "foo", "bar"))

        self.assertEqual(
            [["bar", "baz"]], g.word_paths(["foo", "baz", "qux"], "bar", "baz")
        )
        self.assertEqual(
            [["der", "dfr", "dfs"], ["der", "des", "dfs"]],
            g.word_paths(["des", "der", "dfr", "dgt", "dfs"], "der", "dfs"),
        )
        self.assertEqual(
            [["dep", "dfp", "dfs"], ["dep", "des", "dfs"]],
            g.word_paths(["des", "der", "dfp", "dgt", "dfs"], "dep", "dfs"),
        )
        self.assertEqual(
            [
                ["lkljl", "ljljl", "ljlll", "ljkll"],
                ["lkljl", "lklll", "ljlll", "ljkll"],
            ],
            g.word_paths(WORDS, "lkljl", "ljkll"),
        )


# Test set for graph problems using a word list as adjacency list.
WORDS = tuple(
    map(
        str.strip,
        """\
        ljjjk
        ljjll
        kklll
        jklkl
        lkjkk
        klklk
        llkjj
        ljlll
        kjjlk
        jljjj
        jlkjk
        kjjjk
        llklk
        lklll
        llkkj
        jkllk
        jjllk
        kkljl
        llljk
        kkkkl
        lljkj
        ljkll
        jklkj
        jklkk
        kjllj
        ljllk
        jlkjl
        jjjlj
        kjjjl
        jjlll
        jjjjj
        klllj
        kjlkj
        lkjjj
        kkjlj
        llkkl
        jjjjl
        kjkll
        jkjjk
        ljljl
        kklkj
        jjkkj
        kjkkl
        jllkj
        lkjkj
        lkjjk
        jjljl
        kjjkl
        jkjlk
        lljlk
        kkllj
        jkkkj
        ljkjj
        klkjk
        ljjjj
        kkjkj
        lkllk
        jkllj
        lljjj
        kljkk
        ljjjl
        kkllk
        kljlk
        lkklk
        jljll
        llkll
        jjkjk
        jlkkl
        llkjl
        kkjkk
        kjkkk
        kkklj
        jkkjj
        kjklk
        klkjj
        jlkkk
        lkljj
        klkkj
        jlkll""".splitlines(),
    )
)
