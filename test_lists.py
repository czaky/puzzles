import unittest
from lists import *

class TestLinkedLists(unittest.TestCase):

    def test_make_linked(self):
        self.assertIsNone(make_linked([]))

        n = make_linked([0, 1, 2])
        self.assertEqual(0, n.data)
        n = n.next
        self.assertEqual(1, n.data)
        n = n.next
        self.assertEqual(2, n.data)
        self.assertIsNone(n.next)

    def test_middle(self):
        self.assertIsNone(middle(make_linked([])))

        self.assertEqual(1, middle(make_linked([1])).data)
        self.assertEqual(2, middle(make_linked([1, 2])).data)
        self.assertEqual(2, middle(make_linked([1, 2, 3])).data)
        self.assertEqual(3, middle(make_linked([1, 2, 3, 4])).data)