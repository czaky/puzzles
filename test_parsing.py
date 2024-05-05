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
        """Test the `parse_binop_expression` parser."""
        assert parse_binop_expression("a") == "a"
        assert parse_binop_expression("a+b") == ("+", "a", "b")

        assert parse_binop_expression("a+b+c") == ("+", ("+", "a", "b"), "c")
        assert parse_binop_expression("(a+b)+c") == ("+", ("+", "a", "b"), "c")
        assert parse_binop_expression("a+(b+c)") == ("+", "a", ("+", "b", "c"))

        assert parse_binop_expression("a-b-c") == ("-", ("-", "a", "b"), "c")
        assert parse_binop_expression("(a-b)-c") == ("-", ("-", "a", "b"), "c")
        assert parse_binop_expression("a-(b-c)") == ("-", "a", ("-", "b", "c"))

        assert parse_binop_expression("a-b+c") == ("+", ("-", "a", "b"), "c")
        assert parse_binop_expression("(a-b)+c") == ("+", ("-", "a", "b"), "c")
        assert parse_binop_expression("a-(b+c)") == ("-", "a", ("+", "b", "c"))

        assert parse_binop_expression("a+b-c") == ("-", ("+", "a", "b"), "c")
        assert parse_binop_expression("(a+b)-c") == ("-", ("+", "a", "b"), "c")
        assert parse_binop_expression("a+(b-c)") == ("+", "a", ("-", "b", "c"))

        assert parse_binop_expression("a*b*c") == ("*", ("*", "a", "b"), "c")
        assert parse_binop_expression("(a*b)*c") == ("*", ("*", "a", "b"), "c")
        assert parse_binop_expression("a*(b*c)") == ("*", "a", ("*", "b", "c"))

        assert parse_binop_expression("a+(b*c)") == ("+", "a", ("*", "b", "c"))
        assert parse_binop_expression("(a+b)*c") == ("*", ("+", "a", "b"), "c")
        assert parse_binop_expression("a+(b*c)") == ("+", "a", ("*", "b", "c"))

        assert parse_binop_expression("a*b+c") == ("+", ("*", "a", "b"), "c")
        assert parse_binop_expression("(a*b)+c") == ("+", ("*", "a", "b"), "c")
        assert parse_binop_expression("a*(b+c)") == ("*", "a", ("+", "b", "c"))

        assert parse_binop_expression("a/b/c") == ("/", ("/", "a", "b"), "c")
        assert parse_binop_expression("(a/b)/c") == ("/", ("/", "a", "b"), "c")
        assert parse_binop_expression("a/(b/c)") == ("/", "a", ("/", "b", "c"))

        assert parse_binop_expression("a*b/c") == ("/", ("*", "a", "b"), "c")
        assert parse_binop_expression("(a*b)/c") == ("/", ("*", "a", "b"), "c")
        assert parse_binop_expression("a*(b/c)") == ("*", "a", ("/", "b", "c"))

        assert parse_binop_expression("a/b*c") == ("*", ("/", "a", "b"), "c")
        assert parse_binop_expression("(a/b)*c") == ("*", ("/", "a", "b"), "c")
        assert parse_binop_expression("a/(b*c)") == ("/", "a", ("*", "b", "c"))

    def test_simplify_binops_brackets(self):  # noqa: PLR0915
        """Test the `simplify_binops_brackets` parser."""
        assert simplify_binops_brackets("a") == "a"
        assert simplify_binops_brackets("a+b") == "a+b"

        assert simplify_binops_brackets("a+b+c") == "a+b+c"
        assert simplify_binops_brackets("(a+b)+c") == "a+b+c"
        assert simplify_binops_brackets("a+(b+c)") == "a+b+c"

        assert simplify_binops_brackets("a-b-c") == "a-b-c"
        assert simplify_binops_brackets("(a-b)-c") == "a-b-c"
        assert simplify_binops_brackets("a-(b-c)") == "a-(b-c)"

        assert simplify_binops_brackets("a-b+c") == "a-b+c"
        assert simplify_binops_brackets("(a-b)+c") == "a-b+c"
        assert simplify_binops_brackets("a-(b+c)") == "a-(b+c)"

        assert simplify_binops_brackets("a+b-c") == "a+b-c"
        assert simplify_binops_brackets("(a+b)-c") == "a+b-c"
        assert simplify_binops_brackets("a+(b-c)") == "a+b-c"

        assert simplify_binops_brackets("a*b*c") == "a*b*c"
        assert simplify_binops_brackets("(a*b)*c") == "a*b*c"
        assert simplify_binops_brackets("a*(b*c)") == "a*b*c"

        assert simplify_binops_brackets("a+(b*c)") == "a+b*c"
        assert simplify_binops_brackets("(a+b)*c") == "(a+b)*c"
        assert simplify_binops_brackets("a+(b*c)") == "a+b*c"

        assert simplify_binops_brackets("a*b+c") == "a*b+c"
        assert simplify_binops_brackets("(a*b)+c") == "a*b+c"
        assert simplify_binops_brackets("a*(b+c)") == "a*(b+c)"

        assert simplify_binops_brackets("a/b/c") == "a/b/c"
        assert simplify_binops_brackets("(a/b)/c") == "a/b/c"
        assert simplify_binops_brackets("a/(b/c)") == "a/(b/c)"

        assert simplify_binops_brackets("a*b/c") == "a*b/c"
        assert simplify_binops_brackets("(a*b)/c") == "a*b/c"
        assert simplify_binops_brackets("a*(b/c)") == "a*b/c"

        assert simplify_binops_brackets("a/b*c") == "a/b*c"
        assert simplify_binops_brackets("(a/b)*c") == "a/b*c"
        assert simplify_binops_brackets("a/(b*c)") == "a/(b*c)"

        assert simplify_binops_brackets("a+(b/c)") == "a+b/c"
        assert simplify_binops_brackets("(a+b)/c") == "(a+b)/c"
        assert simplify_binops_brackets("a+(b/c)") == "a+b/c"

        assert simplify_binops_brackets("a/b+c") == "a/b+c"
        assert simplify_binops_brackets("(a/b)+c") == "a/b+c"
        assert simplify_binops_brackets("a/(b+c)") == "a/(b+c)"

        assert simplify_binops_brackets("a-b/c") == "a-b/c"
        assert simplify_binops_brackets("(a-b)/c") == "(a-b)/c"
        assert simplify_binops_brackets("a-(b/c)") == "a-b/c"

        assert simplify_binops_brackets("a-b*c") == "a-b*c"
        assert simplify_binops_brackets("(a-b)*c") == "(a-b)*c"
        assert simplify_binops_brackets("a-(b*c)") == "a-b*c"

        assert simplify_binops_brackets("a/b-c") == "a/b-c"
        assert simplify_binops_brackets("(a/b)-c") == "a/b-c"
        assert simplify_binops_brackets("a/(b-c)") == "a/(b-c)"

        assert simplify_binops_brackets("a*b-c") == "a*b-c"
        assert simplify_binops_brackets("(a*b)-c") == "a*b-c"
        assert simplify_binops_brackets("a*(b-c)") == "a*(b-c)"

    def test_simplify_binops_brackets_one_pass(self):  # noqa: PLR0915
        """Test the `simplify_binops_brackets_one_pass` parser."""
        assert simplify_binops_brackets_one_pass("a") == "a"
        assert simplify_binops_brackets_one_pass("a+b") == "a+b"

        assert simplify_binops_brackets_one_pass("a+b+c") == "a+b+c"
        assert simplify_binops_brackets_one_pass("(a+b)+c") == "a+b+c"
        assert simplify_binops_brackets_one_pass("a+(b+c)") == "a+b+c"

        assert simplify_binops_brackets_one_pass("a-b-c") == "a-b-c"
        assert simplify_binops_brackets_one_pass("(a-b)-c") == "a-b-c"
        assert simplify_binops_brackets_one_pass("a-(b-c)") == "a-(b-c)"

        assert simplify_binops_brackets_one_pass("a-b+c") == "a-b+c"
        assert simplify_binops_brackets_one_pass("(a-b)+c") == "a-b+c"
        assert simplify_binops_brackets_one_pass("a-(b+c)") == "a-(b+c)"

        assert simplify_binops_brackets_one_pass("a+b-c") == "a+b-c"
        assert simplify_binops_brackets_one_pass("(a+b)-c") == "a+b-c"
        assert simplify_binops_brackets_one_pass("a+(b-c)") == "a+b-c"

        assert simplify_binops_brackets_one_pass("a*b*c") == "a*b*c"
        assert simplify_binops_brackets_one_pass("(a*b)*c") == "a*b*c"
        assert simplify_binops_brackets_one_pass("a*(b*c)") == "a*b*c"

        assert simplify_binops_brackets_one_pass("a+(b*c)") == "a+b*c"
        assert simplify_binops_brackets_one_pass("(a+b)*c") == "(a+b)*c"
        assert simplify_binops_brackets_one_pass("a+(b*c)") == "a+b*c"

        assert simplify_binops_brackets_one_pass("a*b+c") == "a*b+c"
        assert simplify_binops_brackets_one_pass("(a*b)+c") == "a*b+c"
        assert simplify_binops_brackets_one_pass("a*(b+c)") == "a*(b+c)"

        assert simplify_binops_brackets_one_pass("a/b/c") == "a/b/c"
        assert simplify_binops_brackets_one_pass("(a/b)/c") == "a/b/c"
        assert simplify_binops_brackets_one_pass("a/(b/c)") == "a/(b/c)"

        assert simplify_binops_brackets_one_pass("a*b/c") == "a*b/c"
        assert simplify_binops_brackets_one_pass("(a*b)/c") == "a*b/c"
        assert simplify_binops_brackets_one_pass("a*(b/c)") == "a*b/c"

        assert simplify_binops_brackets_one_pass("a/b*c") == "a/b*c"
        assert simplify_binops_brackets_one_pass("(a/b)*c") == "a/b*c"
        assert simplify_binops_brackets_one_pass("a/(b*c)") == "a/(b*c)"

        assert simplify_binops_brackets_one_pass("a+(b/c)") == "a+b/c"
        assert simplify_binops_brackets_one_pass("(a+b)/c") == "(a+b)/c"
        assert simplify_binops_brackets_one_pass("a+(b/c)") == "a+b/c"

        assert simplify_binops_brackets_one_pass("a/b+c") == "a/b+c"
        assert simplify_binops_brackets_one_pass("(a/b)+c") == "a/b+c"
        assert simplify_binops_brackets_one_pass("a/(b+c)") == "a/(b+c)"

        assert simplify_binops_brackets_one_pass("a-b/c") == "a-b/c"
        assert simplify_binops_brackets_one_pass("(a-b)/c") == "(a-b)/c"
        assert simplify_binops_brackets_one_pass("a-(b/c)") == "a-b/c"

        assert simplify_binops_brackets_one_pass("a-b*c") == "a-b*c"
        assert simplify_binops_brackets_one_pass("(a-b)*c") == "(a-b)*c"
        assert simplify_binops_brackets_one_pass("a-(b*c)") == "a-b*c"

        assert simplify_binops_brackets_one_pass("a/b-c") == "a/b-c"
        assert simplify_binops_brackets_one_pass("(a/b)-c") == "a/b-c"
        assert simplify_binops_brackets_one_pass("a/(b-c)") == "a/(b-c)"

        assert simplify_binops_brackets_one_pass("a*b-c") == "a*b-c"
        assert simplify_binops_brackets_one_pass("(a*b)-c") == "a*b-c"
        assert simplify_binops_brackets_one_pass("a*(b-c)") == "a*(b-c)"
