"""Test module for parsing related puzzles."""

import unittest

from parsing import (
    parse_binop_expression,
    simplify_binops_brackets,
    simplify_binops_brackets_one_pass,
)


class TestParsing(unittest.TestCase):
    """Test class for the parsing puzzles."""

    def test_parse_binop_expression(self):
        "Test the `parse_binop_expression` parser."
        self.assertEqual("a", parse_binop_expression("a"))
        self.assertEqual(("+", "a", "b"), parse_binop_expression("a+b"))

        self.assertEqual(("+", ("+", "a", "b"), "c"), parse_binop_expression("a+b+c"))
        self.assertEqual(("+", ("+", "a", "b"), "c"), parse_binop_expression("(a+b)+c"))
        self.assertEqual(("+", "a", ("+", "b", "c")), parse_binop_expression("a+(b+c)"))

        self.assertEqual(("-", ("-", "a", "b"), "c"), parse_binop_expression("a-b-c"))
        self.assertEqual(("-", ("-", "a", "b"), "c"), parse_binop_expression("(a-b)-c"))
        self.assertEqual(("-", "a", ("-", "b", "c")), parse_binop_expression("a-(b-c)"))

        self.assertEqual(("+", ("-", "a", "b"), "c"), parse_binop_expression("a-b+c"))
        self.assertEqual(("+", ("-", "a", "b"), "c"), parse_binop_expression("(a-b)+c"))
        self.assertEqual(("-", "a", ("+", "b", "c")), parse_binop_expression("a-(b+c)"))

        self.assertEqual(("-", ("+", "a", "b"), "c"), parse_binop_expression("a+b-c"))
        self.assertEqual(("-", ("+", "a", "b"), "c"), parse_binop_expression("(a+b)-c"))
        self.assertEqual(("+", "a", ("-", "b", "c")), parse_binop_expression("a+(b-c)"))

        self.assertEqual(("*", ("*", "a", "b"), "c"), parse_binop_expression("a*b*c"))
        self.assertEqual(("*", ("*", "a", "b"), "c"), parse_binop_expression("(a*b)*c"))
        self.assertEqual(("*", "a", ("*", "b", "c")), parse_binop_expression("a*(b*c)"))

        self.assertEqual(("+", "a", ("*", "b", "c")), parse_binop_expression("a+(b*c)"))
        self.assertEqual(("*", ("+", "a", "b"), "c"), parse_binop_expression("(a+b)*c"))
        self.assertEqual(("+", "a", ("*", "b", "c")), parse_binop_expression("a+(b*c)"))

        self.assertEqual(("+", ("*", "a", "b"), "c"), parse_binop_expression("a*b+c"))
        self.assertEqual(("+", ("*", "a", "b"), "c"), parse_binop_expression("(a*b)+c"))
        self.assertEqual(("*", "a", ("+", "b", "c")), parse_binop_expression("a*(b+c)"))

        self.assertEqual(("/", ("/", "a", "b"), "c"), parse_binop_expression("a/b/c"))
        self.assertEqual(("/", ("/", "a", "b"), "c"), parse_binop_expression("(a/b)/c"))
        self.assertEqual(("/", "a", ("/", "b", "c")), parse_binop_expression("a/(b/c)"))

        self.assertEqual(("/", ("*", "a", "b"), "c"), parse_binop_expression("a*b/c"))
        self.assertEqual(("/", ("*", "a", "b"), "c"), parse_binop_expression("(a*b)/c"))
        self.assertEqual(("*", "a", ("/", "b", "c")), parse_binop_expression("a*(b/c)"))

        self.assertEqual(("*", ("/", "a", "b"), "c"), parse_binop_expression("a/b*c"))
        self.assertEqual(("*", ("/", "a", "b"), "c"), parse_binop_expression("(a/b)*c"))
        self.assertEqual(("/", "a", ("*", "b", "c")), parse_binop_expression("a/(b*c)"))

    def test_simplify_binops_brackets(self):
        "Test the `simplify_binops_brackets` parser."
        self.assertEqual("a", simplify_binops_brackets("a"))
        self.assertEqual("a+b", simplify_binops_brackets("a+b"))

        self.assertEqual("a+b+c", simplify_binops_brackets("a+b+c"))
        self.assertEqual("a+b+c", simplify_binops_brackets("(a+b)+c"))
        self.assertEqual("a+b+c", simplify_binops_brackets("a+(b+c)"))

        self.assertEqual("a-b-c", simplify_binops_brackets("a-b-c"))
        self.assertEqual("a-b-c", simplify_binops_brackets("(a-b)-c"))
        self.assertEqual("a-(b-c)", simplify_binops_brackets("a-(b-c)"))

        self.assertEqual("a-b+c", simplify_binops_brackets("a-b+c"))
        self.assertEqual("a-b+c", simplify_binops_brackets("(a-b)+c"))
        self.assertEqual("a-(b+c)", simplify_binops_brackets("a-(b+c)"))

        self.assertEqual("a+b-c", simplify_binops_brackets("a+b-c"))
        self.assertEqual("a+b-c", simplify_binops_brackets("(a+b)-c"))
        self.assertEqual("a+b-c", simplify_binops_brackets("a+(b-c)"))

        self.assertEqual("a*b*c", simplify_binops_brackets("a*b*c"))
        self.assertEqual("a*b*c", simplify_binops_brackets("(a*b)*c"))
        self.assertEqual("a*b*c", simplify_binops_brackets("a*(b*c)"))

        self.assertEqual("a+b*c", simplify_binops_brackets("a+(b*c)"))
        self.assertEqual("(a+b)*c", simplify_binops_brackets("(a+b)*c"))
        self.assertEqual("a+b*c", simplify_binops_brackets("a+(b*c)"))

        self.assertEqual("a*b+c", simplify_binops_brackets("a*b+c"))
        self.assertEqual("a*b+c", simplify_binops_brackets("(a*b)+c"))
        self.assertEqual("a*(b+c)", simplify_binops_brackets("a*(b+c)"))

        self.assertEqual("a/b/c", simplify_binops_brackets("a/b/c"))
        self.assertEqual("a/b/c", simplify_binops_brackets("(a/b)/c"))
        self.assertEqual("a/(b/c)", simplify_binops_brackets("a/(b/c)"))

        self.assertEqual("a*b/c", simplify_binops_brackets("a*b/c"))
        self.assertEqual("a*b/c", simplify_binops_brackets("(a*b)/c"))
        self.assertEqual("a*b/c", simplify_binops_brackets("a*(b/c)"))

        self.assertEqual("a/b*c", simplify_binops_brackets("a/b*c"))
        self.assertEqual("a/b*c", simplify_binops_brackets("(a/b)*c"))
        self.assertEqual("a/(b*c)", simplify_binops_brackets("a/(b*c)"))

        self.assertEqual("a+b/c", simplify_binops_brackets("a+(b/c)"))
        self.assertEqual("(a+b)/c", simplify_binops_brackets("(a+b)/c"))
        self.assertEqual("a+b/c", simplify_binops_brackets("a+(b/c)"))

        self.assertEqual("a/b+c", simplify_binops_brackets("a/b+c"))
        self.assertEqual("a/b+c", simplify_binops_brackets("(a/b)+c"))
        self.assertEqual("a/(b+c)", simplify_binops_brackets("a/(b+c)"))

        self.assertEqual("a-b/c", simplify_binops_brackets("a-b/c"))
        self.assertEqual("(a-b)/c", simplify_binops_brackets("(a-b)/c"))
        self.assertEqual("a-b/c", simplify_binops_brackets("a-(b/c)"))

        self.assertEqual("a-b*c", simplify_binops_brackets("a-b*c"))
        self.assertEqual("(a-b)*c", simplify_binops_brackets("(a-b)*c"))
        self.assertEqual("a-b*c", simplify_binops_brackets("a-(b*c)"))

        self.assertEqual("a/b-c", simplify_binops_brackets("a/b-c"))
        self.assertEqual("a/b-c", simplify_binops_brackets("(a/b)-c"))
        self.assertEqual("a/(b-c)", simplify_binops_brackets("a/(b-c)"))

        self.assertEqual("a*b-c", simplify_binops_brackets("a*b-c"))
        self.assertEqual("a*b-c", simplify_binops_brackets("(a*b)-c"))
        self.assertEqual("a*(b-c)", simplify_binops_brackets("a*(b-c)"))

    def test_simplify_binops_brackets_one_pass(self):
        "Test the `simplify_binops_brackets_one_pass` parser."
        self.assertEqual("a", simplify_binops_brackets_one_pass("a"))
        self.assertEqual("a+b", simplify_binops_brackets_one_pass("a+b"))

        self.assertEqual("a+b+c", simplify_binops_brackets_one_pass("a+b+c"))
        self.assertEqual("a+b+c", simplify_binops_brackets_one_pass("(a+b)+c"))
        self.assertEqual("a+b+c", simplify_binops_brackets_one_pass("a+(b+c)"))

        self.assertEqual("a-b-c", simplify_binops_brackets_one_pass("a-b-c"))
        self.assertEqual("a-b-c", simplify_binops_brackets_one_pass("(a-b)-c"))
        self.assertEqual("a-(b-c)", simplify_binops_brackets_one_pass("a-(b-c)"))

        self.assertEqual("a-b+c", simplify_binops_brackets_one_pass("a-b+c"))
        self.assertEqual("a-b+c", simplify_binops_brackets_one_pass("(a-b)+c"))
        self.assertEqual("a-(b+c)", simplify_binops_brackets_one_pass("a-(b+c)"))

        self.assertEqual("a+b-c", simplify_binops_brackets_one_pass("a+b-c"))
        self.assertEqual("a+b-c", simplify_binops_brackets_one_pass("(a+b)-c"))
        self.assertEqual("a+b-c", simplify_binops_brackets_one_pass("a+(b-c)"))

        self.assertEqual("a*b*c", simplify_binops_brackets_one_pass("a*b*c"))
        self.assertEqual("a*b*c", simplify_binops_brackets_one_pass("(a*b)*c"))
        self.assertEqual("a*b*c", simplify_binops_brackets_one_pass("a*(b*c)"))

        self.assertEqual("a+b*c", simplify_binops_brackets_one_pass("a+(b*c)"))
        self.assertEqual("(a+b)*c", simplify_binops_brackets_one_pass("(a+b)*c"))
        self.assertEqual("a+b*c", simplify_binops_brackets_one_pass("a+(b*c)"))

        self.assertEqual("a*b+c", simplify_binops_brackets_one_pass("a*b+c"))
        self.assertEqual("a*b+c", simplify_binops_brackets_one_pass("(a*b)+c"))
        self.assertEqual("a*(b+c)", simplify_binops_brackets_one_pass("a*(b+c)"))

        self.assertEqual("a/b/c", simplify_binops_brackets_one_pass("a/b/c"))
        self.assertEqual("a/b/c", simplify_binops_brackets_one_pass("(a/b)/c"))
        self.assertEqual("a/(b/c)", simplify_binops_brackets_one_pass("a/(b/c)"))

        self.assertEqual("a*b/c", simplify_binops_brackets_one_pass("a*b/c"))
        self.assertEqual("a*b/c", simplify_binops_brackets_one_pass("(a*b)/c"))
        self.assertEqual("a*b/c", simplify_binops_brackets_one_pass("a*(b/c)"))

        self.assertEqual("a/b*c", simplify_binops_brackets_one_pass("a/b*c"))
        self.assertEqual("a/b*c", simplify_binops_brackets_one_pass("(a/b)*c"))
        self.assertEqual("a/(b*c)", simplify_binops_brackets_one_pass("a/(b*c)"))

        self.assertEqual("a+b/c", simplify_binops_brackets_one_pass("a+(b/c)"))
        self.assertEqual("(a+b)/c", simplify_binops_brackets_one_pass("(a+b)/c"))
        self.assertEqual("a+b/c", simplify_binops_brackets_one_pass("a+(b/c)"))

        self.assertEqual("a/b+c", simplify_binops_brackets_one_pass("a/b+c"))
        self.assertEqual("a/b+c", simplify_binops_brackets_one_pass("(a/b)+c"))
        self.assertEqual("a/(b+c)", simplify_binops_brackets_one_pass("a/(b+c)"))

        self.assertEqual("a-b/c", simplify_binops_brackets_one_pass("a-b/c"))
        self.assertEqual("(a-b)/c", simplify_binops_brackets_one_pass("(a-b)/c"))
        self.assertEqual("a-b/c", simplify_binops_brackets_one_pass("a-(b/c)"))

        self.assertEqual("a-b*c", simplify_binops_brackets_one_pass("a-b*c"))
        self.assertEqual("(a-b)*c", simplify_binops_brackets_one_pass("(a-b)*c"))
        self.assertEqual("a-b*c", simplify_binops_brackets_one_pass("a-(b*c)"))

        self.assertEqual("a/b-c", simplify_binops_brackets_one_pass("a/b-c"))
        self.assertEqual("a/b-c", simplify_binops_brackets_one_pass("(a/b)-c"))
        self.assertEqual("a/(b-c)", simplify_binops_brackets_one_pass("a/(b-c)"))

        self.assertEqual("a*b-c", simplify_binops_brackets_one_pass("a*b-c"))
        self.assertEqual("a*b-c", simplify_binops_brackets_one_pass("(a*b)-c"))
        self.assertEqual("a*(b-c)", simplify_binops_brackets_one_pass("a*(b-c)"))
