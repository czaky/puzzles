"Algorithms used to parse and process formal languages."

from typing import List


def parse_binop_expression(tokens: list) -> tuple:
    """Parses an arithmetic expression consisting of literals and operators from '+-*/()'.

    The parsed expression is represented as tripples of the form:
        (<operator>, <arg1>, <arg2>)

    Parameters:
        tokens (list): tokenized expression consisting of operators '+-*/()' and literals.

    Returns:
        tuple: the root of the parsed expression as (<operator>, <arg1>, <arg2>)
    """
    # The implementation here avoids recursion and uses two stacks
    # similar to the  Dijkstra's Shunting Yard algorithm.

    # Stores the arguments and successive parsed results of the expression.
    args = []
    # Stores the operators seen so far.
    # The ops arrays should contains "+-(" and at most one of "*/".
    # Note that we start with an implicit bracket.
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
            rargs.append((rops.pop(), rargs.pop(), rargs.pop()))
        # The final expression is moved back onto the stack.
        args.append(rargs.pop())

    for t in tokens:
        # Push all operators onto the `ops` stack
        # except for the closing bracket.
        if t in "*/+-(":
            ops.append(t)
            continue

        if t == ")":
            # Closing bracket forms on new expression on the args stack.
            close_bracket()
        else:
            # Push remaining args onto the stack.
            args.append(t)

        # Given a new expression on the stack from above,
        # we can now form any "*/" expressions if possible.
        # This removes all the "*/" expressions from the ops stack.
        while ops[-1] in "*/":
            b, a = args.pop(), args.pop()
            args.append((ops.pop(), a, b))

    # Finally, we close the first implicit bracket.
    close_bracket()
    # And return the remaining only expression on the args stack.
    assert len(args) == 1
    return args[0]


def format_binop_expression(e: str | tuple) -> str:
    "Format expressions consisting of (<operator>, <arg1>, <arg2>)."
    if isinstance(e, str):
        return e
    # This is a depth first, iterative algorithm using two stacks.
    s: List[tuple] = []
    v: List[str | tuple] = []
    n: tuple | str | None = e
    # Flatten an expression.
    f = lambda v: v if isinstance(v, str) else v[1]

    def fop(op: str, a: str | tuple, b: str | tuple) -> tuple:
        "Format an operation adding parantheses to the arguments if needed."

        def p(v):
            if isinstance(v, str) or op == "+" or op in "*-" and v[0] in "*/":
                return f(v)
            return "(" + f(v) + ")"

        # Returns the operator and the string representation.
        # We keep the operator so it is easier to know the type of the expression later.
        return op, f(a) + op + p(b)

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
            v.append(fop(n[0], lv, rv))
            n = None
    return f(v[0])
