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

    def test_nth(self):
        "Test `nth` function."
        l = lists.make_linked([1, 2, 3, 4])
        self.assertEqual(1, lists.nth(l, 0).data)
        self.assertEqual(4, lists.nth(l, 3).data)
        self.assertEqual(4, lists.nth(l, -1).data)
        self.assertEqual(1, lists.nth(l, -4).data)
        self.assertIsNone(lists.nth(l, 4))
        self.assertIsNone(lists.nth(l, -5))

        e = lists.make_linked([])
        self.assertIsNone(lists.nth(e, 0))
        self.assertIsNone(lists.nth(e, 1000))
        self.assertIsNone(lists.nth(e, -1000))
