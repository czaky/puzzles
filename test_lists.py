"""Test module for the linked lists puzzles."""
import unittest
import lists

class TestLinkedLists(unittest.TestCase):
    """Test class for the linked lists puzzles."""
    def test_make_linked(self):
        "Test `make_linked`."
        self.assertIsNone(lists.make_linked([]))

        n = lists.make_linked([0, 1, 2])
        self.assertEqual(0, n.data)
        n = n.next
        self.assertEqual(1, n.data)
        n = n.next
        self.assertEqual(2, n.data)
        self.assertIsNone(n.next)

    def test_middle(self):
        "Test `middle` node function."
        self.assertIsNone(lists.middle(lists.make_linked([])))

        self.assertEqual(1, lists.middle(lists.make_linked([1])).data)
        self.assertEqual(2, lists.middle(lists.make_linked([1, 2])).data)
        self.assertEqual(2, lists.middle(lists.make_linked([1, 2, 3])).data)
        self.assertEqual(3, lists.middle(lists.make_linked([1, 2, 3, 4])).data)
