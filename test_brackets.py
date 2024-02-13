import unittest
from brackets import *

class TestBrackets(unittest.TestCase):
    
    def test_balanced(self):
        self.assertTrue(balanced("({[()[]]})"))
        self.assertTrue(balanced("{}[]()"))
        self.assertFalse(balanced("{}[]()["))
        self.assertFalse(balanced("){}[]()"))
        self.assertFalse(balanced("{)[]()"))
