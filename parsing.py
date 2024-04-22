"Algorithms used to parse and process formal languages."

from typing import Callable, List, Sequence, Tuple


def expression_tuple(*args):
    "Return args as a tuple."
    return args


def parse_binop_expression(tokens: Sequence, make: Callable = expression_tuple):
    """Parses an arithmetic expression consisting of literals and operators from '+-*/()'.

    The parsed expression is represented as triples of the form:
        (<operator>, <arg1>, <arg2>)
    Alternatively, a `make` function can be passed in for alternative representation.

    Parameters:
        tokens (Sequence): tokenized expression consisting of operators '+-*/()' and literals.
        make (Callable): generates binary expression objects out of arguments.

    Returns:
        any: the root of the parsed expression (as returned by the `make` function).
    """
    # The implementation here avoids recursion and uses two stacks
    # similar to the  Dijkstra's Shunting Yard algorithm.

    # Stores the arguments and successive parsed results of the expression.
    args = []
    # Stores the operators seen so far.
    # The ops array should only contain "+-(" and at most one of "*/".
    # Start with an implicit, opening bracket.
    ops = ["("]

    def close_bracket():
        # This is called when we close and process a (bracketed) sub-expression
        #
        # The remaining operators here are "+-".
        # The idea is to first reverse the operators and their arguments.
        rargs = [args.pop()]
        rops = []
        while ops[-1] in "+-":
            rargs.append(args.pop())
            rops.append(ops.pop())
        # We should have arrived at the opening bracket.
        assert ops.pop() == "("
        # Apply the operators (in reversed order) to form the expressions.
        while rops:
            rargs.append(make(rops.pop(), rargs.pop(), rargs.pop()))
        # The final expression is moved back onto the stack.
        return rargs.pop()

    for t in tokens:
        # Push all operators onto the `ops` stack
        # except for the closing bracket.
        if t in "*/+-(":
            ops.append(t)
            continue

        # Push remaining args onto the stack.
        # Closing bracket also forms a new expression on the args stack.
        args.append(close_bracket() if t == ")" else t)

        # Given a new expression on the stack from above,
        # we can now form any "*/" expressions if possible.
        # This removes all the "*/" expressions from the ops stack.
        while ops[-1] in "*/":
            b, a = args.pop(), args.pop()
            args.append(make(ops.pop(), a, b))

    # Finally, we close the initial, implicit bracket.
    return close_bracket()


def simplified_binop_expression_factory() -> Tuple[Callable, Callable]:
    "Returns an expression formatter and a string extractor."
    # Define the grammar:
    # Precedence rank of the operators.
    rank = {"*": 1, "/": 1, "+": 2, "-": 2}
    # Do the operators need brackets for the right term?
    commutative_operators = "+*"

    # Is `v` a leaf (string) node?
    leaf = lambda v: isinstance(v, str)
    # Flatten a node into a string?
    flat = lambda v: v if leaf(v) else v[1]
    # Make a string out of argument `v` and surround it with brackets if necessary.
    form = lambda v, flt: flat(v) if flt else "(" + flat(v) + ")"

    def fop(op: str, a: str | tuple, b: str | tuple) -> tuple:
        "Format an operation adding parentheses to the arguments if needed."
        l = form(a, leaf(a) or rank[a[0]] <= rank[op])
        r = form(b, leaf(b) or rank[b[0]] < rank[op] + (op in commutative_operators))
        # Returns the operator and the string representation.
        # We keep the operator so it is easier to know the type of the expression later.
        return op, l + op + r

    return fop, flat


def simplify_binops_brackets_one_pass(tokens: Sequence) -> str:
    "Remove redundant brackets from the expression in one pass."
    # Provides an expression constructor, and
    # an `extract` function to extract the string representation
    # from the final expression.
    expression, extract = simplified_binop_expression_factory()

    return extract(parse_binop_expression(tokens, make=expression))


def format_binop_expression(
    e: str | tuple, factory=simplified_binop_expression_factory
) -> str:
    "Format expressions consisting of (<operator>, <arg1>, <arg2>)."
    if isinstance(e, str):
        return e
    # This is a depth first, iterative algorithm using two stacks.
    s: List[tuple] = []
    v: List[str | tuple] = []
    n: tuple | str | None = e

    # Provides an expression `factory`, and
    # the `extract` function to extract the string representation
    # from the final expression.
    expression, extract = factory()

    while s or n:
        # Repeatedly, descend left from node.
        while isinstance(n, tuple):
            # If this is on the stack, we consume the node.
            s.append(n)
            # If this is on the stack, we descend right.
            s.append(n)
            n = n[1]
        if n is not None:
            v.append(n)
        n = s.pop()
        if s and s[-1] == n:
            # Descend right from node.
            n = n[2]
        else:
            # Consume this node and
            # generate intermediate values.
            rv, lv = v.pop(), v.pop()
            v.append(expression(n[0], lv, rv))
            n = None

    return extract(v[0])


def simplify_binops_brackets(tokens: Sequence) -> str:
    "Remove redundant brackets from the expression."
    return format_binop_expression(parse_binop_expression(tokens))
