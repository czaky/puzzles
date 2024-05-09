"""Puzzles related to binary (search) trees."""

from __future__ import annotations

from collections import deque
from functools import reduce
from itertools import islice
from math import inf
from typing import TYPE_CHECKING, Any, Iterator, Optional

if TYPE_CHECKING:
    import lists


class TreeNode:
    """Node of a binary tree."""

    def __init__(self, data: Any) -> None:
        """Return a TreeNode.

        Parameters
        ----------
        data : Any
            Value of the node

        """
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.height: int = 1

    def __bool__(self) -> bool:
        """Return True."""
        return True

    def __len__(self) -> int:
        """Compute the length starting at this node."""
        return 1 + len(self.left or ()) + len(self.right or ())

    def __contains__(self, x: object) -> bool:
        """Return True if x is contained in this tree."""
        return self.data == x or (x in (self.left or ())) or (x in (self.right or ()))

    # Iterators

    def level_order(self, *, nodes: bool = False) -> Iterator:
        """Breadth First Search (level order) iterator.

        Args:
        ----
            nodes (bool, optional): If true, yield nodes instead of values.

        """
        # Iterative implementation using a queue.
        q: deque[Node] = deque([self])
        while q:
            n = q.popleft()
            yield (n if nodes else n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    def __iter__(self) -> Iterator:
        """Return a level order iterator.

        Yields
        ------
        Iterator
            tree values in level order

        """
        # BFS (breadth first search) or level order.
        return self.level_order()

    # Depth first traversals.

    def preorder(self, *, nodes: bool = False) -> Iterator:
        """Pre-order, depth first (DFS) traversal of the binary tree.

        Useful to create a copy of the tree and generate prefix expressions.
        Nodes are enumerated top-down.

        Args:
        ----
            nodes (bool, optional): It true, yield nodes instead of value.

        """
        r: TreeNode = self
        s = [r]
        while s:
            n = s.pop()
            yield (n if nodes else n.data)
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)

    def inorder(self, *, nodes: bool = False) -> Iterator:
        """In-order, depth first (DFS) traversal of the binary tree.

        Useful to sequence a binary search tree (BST) in sorted order.

        Args:
        ----
            nodes (bool, optional): It true, yield nodes instead of value.

        """
        # Iterative implementation using a stack.
        s = []
        n = self
        while s or n:
            while n:
                s.append(n)
                n = n.left
            n = s.pop()
            yield (n if nodes else n.data)
            n = n.right

    def postorder(self, *, nodes: bool = False) -> Iterator:
        """Post-order, depth first (DFS) traversal of the binary tree.

        Useful to delete a tree and to generate a postfix expression.
        Nodes are enumerated bottom-up.

        Args:
        ----
            nodes (bool, optional): It true, yield nodes instead of value.

        """
        s = []
        p = None  # previous
        n: None | Node = self  # current node
        while s or n:
            # descend left
            while n:
                s.append(n)
                n = n.left
            # descend right
            r = s[-1].right
            if r and r != p:
                n = r
            else:
                p = s.pop()
                yield (p if nodes else p.data)

    def iter(self, order: str = "level", *, nodes: bool = False) -> Iterator:
        """Return an iterator for a tree traversal in the specific `order`.

        Args:
        ----
            order (str, optional): One of: "level" (default), "pre", "in", "post"
            nodes (bool, optional): If true, yields nodes instead of values.

        """
        if order == "level":
            yield from self.level_order(nodes=nodes)
        elif order == "pre":
            yield from self.preorder(nodes=nodes)
        elif order == "in":
            yield from self.inorder(nodes=nodes)
        elif order == "post":
            yield from self.postorder(nodes=nodes)
        else:
            msg = "`order` shoul be one of: level, pre, in, or post."
            raise ValueError(msg)

    # Presentation

    def display(self, *, v: bool = False) -> None:
        """Display the tree in a visual 2D manner."""

        def aux(node: Node) -> tuple[list, int, int, int]:
            """-> lines, width, height, middle."""
            s = str(node.data) if not v else f"{node.data}({node.height})"
            u = len(s)

            if not node.left and not node.right:
                return [s], u, 1, u // 2

            # Only left child.
            if not node.right:
                lines, n, p, x = aux(node.left)
                first = (x + 1) * " " + (n - x - 1) * "_" + s
                second = x * " " + "/" + (n - x - 1 + u) * " "
                shifted = [line + u * " " for line in lines]
                return [first, second, *shifted], n + u, p + 2, n + u // 2

            # Only right child.
            if not node.left:
                lines, n, p, x = aux(node.right)
                first = s + x * "_" + (n - x) * " "
                second = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted = [u * " " + line for line in lines]
                return [first, second, *shifted], n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = aux(node.left)
            right, m, q, y = aux(node.right)
            first = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second = (
                x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            )
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            lines = [first, second] + [a + u * " " + b for a, b in zip(left, right)]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        mxl = 0
        for line in aux(self)[0]:
            mxl = max(mxl, len(line))
            mxl = max(mxl, len(line))
            print(line)  # noqa: T201

        if v:
            print("-" * mxl)  # noqa: T201
            print(self)  # noqa: T201
            print("-" * mxl)  # noqa: T201

    def serialize_level_order(self, none: str = "N") -> str:
        """Return a BFS, level-order string representation using none ('N') for None."""
        # Iterative implementation using DFS and a queue.
        o = []
        q: deque[Node] = deque([self])
        while q:
            n = q.popleft()
            o.append(str(n.data) if n else none)
            if n:
                q.append(n.left)
                q.append(n.right)
        while o and o[-1] == none:
            o.pop()
        return " ".join(o)

    def serialize_pre_order(self, none: str = "N") -> str:
        """Return a DFS, pre-order string representation using none ('N') for None."""
        # Iterative implementation using DFS and a stack.
        o = []
        s: list[Node] = [self]
        while s:
            n = s.pop()
            o.append(str(n.data) if n else none)
            if n:
                s.append(n.right)
                s.append(n.left)
        while o and o[-1] == none:
            o.pop()
        return " ".join(o)

    def serialize_in_order(self, lr: str = "()") -> str:
        """Return a DFS, in-order string representation using brackets."""
        lb, rb = lr
        # Iterative implementation using a stack.
        s: list[Node] = []
        v: list[str] = []
        n: Node = self
        while s or n:
            # Descend left from node.
            while n:
                s.append(n)
                s.append(n)
                n = n.left
            n = s.pop()
            if s and s[-1] == n:
                # Descend right from node.
                n = n.right
            else:
                # Consume this node and
                # generate intermediate values.
                mv = str(n.data)
                if n.right:
                    rv = v.pop()
                    lv = v.pop() if n.left else lr
                    v.append(f"{lb}{lv} {mv} {rv}{rb}")
                elif n.left:
                    v.append(f"{lb}{v.pop()} {mv}{rb}")
                else:
                    v.append(mv)
                n = None
        return v[0]

    def serialize_post_order(self, none: str = "N") -> str:
        """Return a DFS, post-order string representation using none ('N') for None."""

        # Recursive implementation using DFS.
        def dfs(n: Node) -> str:
            return f"{dfs(n.left)} {dfs(n.right)} {n.data!s}" if n else none

        return dfs(self)

    def serialize(self, order: str = "level", none: str = "N", lr: str = "()") -> str:
        """Return string representation of `order` using `none` ('N') for `None`.

        Args:
        ----
            none (str): representation for missing node. Defaults to "N".
            order (str): one-of: "level" (default), "pre", "post", "in".
            lr (str): brackets used for in-order representation. Default "()".

        Returns:
        -------
            str: a representation of the tree with 'N' for missing nodes.

        """
        if order == "level":
            return self.serialize_level_order(none)
        if order == "pre":
            return self.serialize_pre_order(none)
        if order == "in":
            return self.serialize_in_order(lr)
        if order == "post":
            return self.serialize_post_order(none)

        msg = "`order` needs to be one of: level, pre, post, or in."
        raise ValueError(msg)

    def __str__(self) -> str:
        """Serialize to level order.

        Returns
        -------
        str
            A string representation of the tree in level order.

        """
        return self.serialize_level_order()

    # Balancing

    def update_height(self) -> None:
        """Update the height of this node based on its children."""
        self.height = 1 + max(height(self.left), height(self.right))

    def left_rotate(self) -> TreeNode:
        """Rotate the tree at this node to the left."""
        #  2_         _4
        # /  \       /  \
        # 1  4   =>  2  5
        #   / \     / \
        #   3 5     1 3
        assert self.right  # noqa: S101
        y = self.right
        self.right = y.left
        y.left = self
        # Update the height of this (lower) node first.
        self.update_height()
        y.update_height()
        return y

    def right_rotate(self) -> TreeNode:
        """Rotate the tree at this node to the right."""
        #   _4         2_
        #  /  \       /  \
        #  2  5   =>  1  4
        # / \           / \
        # 1 3           3 5
        assert self.left  # noqa: S101
        y = self.left
        self.left = y.right
        y.right = self
        # Update the height of this (lower) node first.
        self.update_height()
        y.update_height()
        return y

    def left_skew(self) -> int:
        """Return how far to the left the node is skewed."""
        l, r = self.left, self.right
        return (l.height if l else 0) - (r.height if r else 0)

    def balance_node(self) -> TreeNode:
        """Balance this node. May return one of its descendants."""
        skew = self.left_skew()
        if skew > 1:
            if self.left.left_skew() < 0:
                self.left = self.left.left_rotate()
            return self.right_rotate()
        if skew < -1:
            if self.right.left_skew() > 0:
                self.right = self.right.right_rotate()
            return self.left_rotate()

        self.update_height()
        return self

    def insert_balanced(self, value: int) -> TreeNode:
        """Insert a node with `value`."""
        if value < self.data:
            self.left = insert_balanced(self.left, value)
        elif value > self.data:
            self.right = insert_balanced(self.right, value)
        else:
            return self

        return self.balance_node()

    def delete_balanced(self, value: int) -> Node:
        """Delete the `value` from a self-balancing AVL tree."""
        if value == self.data:
            if not (self.right and self.left):
                return self.left or self.right

            # Find the next in-order successor ...
            min_node = lambda n: n.left and min_node(n.left) or n
            # and use its value.
            value = self.data = min_node(self.right).data
            # The `next_node` will be deleted recursively below.

        if value < self.data:
            self.left = self.left.delete_balanced(value)
        else:
            self.right = self.right.delete_balanced(value)

        return self.balance_node()


Node = Optional[TreeNode]


def height(n: Node) -> int:
    """Return the height of a Node `n` or 0 for NONE."""
    return n.height if n else 0


def make_level_order(s: str, none: str = "N") -> Node:
    """Make a binary tree from a string `s` in breadth first, level order."""
    it = iter(s.split())
    v: None | str = next(it, none)
    if v == none:
        return None
    root = TreeNode(int(v or 0))
    q = deque([root])
    for v in it:
        n = q.popleft()
        if v != none:
            n.left = TreeNode(int(v))
            q.append(n.left)
        u = next(it, None)
        if u is None:
            break
        if u != none:
            n.right = TreeNode(int(u))
            q.append(n.right)
    for n in root.inorder(nodes=True):
        n.update_height()
    return root


def make_pre_order(s: str, none: str = "N") -> Node:
    """Make a binary tree from a string `s` in depth first, pre-order."""

    def des(it: Iterator[str]) -> Node:
        v = next(it, none)
        if v == none:
            return None
        n = TreeNode(int(v))
        n.left = des(it)
        n.right = des(it)
        n.update_height()
        return n

    return des(iter(s.split()))


def make(s: str, order: str = "level", none: str = "N") -> Any:
    """Make a binary tree from string `s` using terminating token `none`.

    Args:
    ----
        s (str): String with values and terminating tokens.
        none (str, optional): Terminating token indicating None. Defaults to "N".
        order (str, optional): One of: 'level', 'pre'. Defaults to "level".

    Returns:
    -------
        Node: A root TreeNode or None.

    """
    if order == "level":
        return make_level_order(s, none)
    if order in ("pre"):
        return make_pre_order(s, none)
    msg = f"Expected `order`(='{order}') to be one of: 'level' or 'pre'"
    raise ValueError(msg)


def inorder_postorder_tangle(inorder: list, post: list) -> Node:
    """Reconstruct a binary tree from its inorder and postorder serialization.

    Parameters
    ----------
    inorder : list
        Elements serialized using in-order DFS.
    post : list
        Elements serialized using post-order DFS.

    Returns
    -------
    Node
        The root of the deserialized tree.

    """
    # Make the index lookup: O(1)
    idx = {v: i for i, v in enumerate(inorder)}

    def r(i: int, j: int) -> Node:
        if i < j:
            # We can just eat the post-order array here.
            n = TreeNode(post[-1])
            m = idx[post.pop()]
            # The right arm comes first in reversed post-order.
            n.right = r(m + 1, j)
            n.left = r(i, m)
            return n
        return None

    return r(0, len(inorder))


def from_list(ln: lists.Node) -> Node:
    """Create a balanced tree from a linked list starting at `ln`."""

    def tree(stop: int) -> Node:
        if stop > 0:
            nonlocal ln
            left = tree(stop // 2)
            tn = TreeNode(ln.data)
            ln = ln.next
            tn.left = left
            tn.right = tree((stop - 1) // 2)
            return tn
        return None

    return tree(len(ln)) if ln else None


def lvo(n: Node, *, nodes: bool = False) -> Iterator:
    """Yield nodes or values in breadth first, level order."""
    if n:
        yield from n.level_order(nodes=nodes)


def ino(n: Node, *, nodes: bool = False) -> Iterator:
    """Yield nodes or values in in-order traversal."""
    if n:
        yield from n.inorder(nodes=nodes)


def left_view(root: Node) -> list:
    """Return the projected left view of the binary tree from `root`."""
    view = []

    def enum(n: Node, level: int) -> None:
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.left, level + 1)
        enum(n.right, level + 1)

    enum(root, 1)
    return view


def right_view(root: Node) -> list:
    """Return the projected right view of the binary tree from `root`."""
    view = []

    def enum(n: Node, level: int) -> None:
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.right, level + 1)
        enum(n.left, level + 1)

    enum(root, 1)
    return view


def reversed_level_order(t: Node) -> list:
    """Return reversed breadth first (level order) enumeration."""
    q = deque([t])
    r = []
    while q:
        n = q.popleft()
        r.append(n.data)
        # append right first
        if n.right:
            q.append(n.right)
        if n.left:
            q.append(n.left)
    return list(reversed(r))


def spiral_order(t: Node) -> list:
    """Return the node values in spiral order.

    Spiral order is alternating from left to right on each level.
    """
    q = deque([t])
    o = []
    lvl = 0
    while q:
        lvl += 1
        ro = []
        for _ in range(len(q)):
            n = q.popleft()
            (ro if lvl % 2 else o).append(n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        o.extend(reversed(ro))
    return o


def insert_balanced(n: Node, value: int) -> TreeNode:
    """Insert a node with `value`."""
    return n.insert_balanced(value) if n else TreeNode(value)


def is_bst(n: Node, mn: float = -inf, mx: float = inf) -> bool:
    """Determine if the binary tree starting at `n` is a BST.

    Parameters
    ----------
    n : Node
        Root of the tree to investigate
    mn : float, optional
        Min value for the tree values, by default -inf
    mx : float, optional
        Max value for the tree values, by default inf

    Returns
    -------
    bool
        True for a BST with values between `mn` and `mx` (inclusive).

    """
    return not n or (
        (mn <= n.data <= mx)
        and is_bst(n.left, mn, n.data - 1)
        and is_bst(n.right, n.data + 1, mx)
    )


def successor(t: Node, x: int) -> Node | None:
    """Return the successor Node in `t` for value `x` in order enumeration."""
    s = []
    n = t
    found = False
    while s or n:
        while n:
            s.append(n)
            n = n.left
        n = s.pop()
        if found:
            return n
        found = n.data == x
        n = n.right
    return None


def largest(r: Node, k: int = 1, default: int = -1) -> int:
    """Return k-largest element from a BST at `r`."""
    # Reverse-order search on the right side.
    s = []
    c = r
    while s or c:
        while c:
            s.append(c)
            c = c.right
        c = s.pop()
        k -= 1
        if k == 0:
            return c.data
        c = c.left
    return default


def balanced(root: Node) -> bool:
    """Return True if tree at `root` is balanced in height."""

    def rank_balance(n: Node) -> tuple[int, bool]:
        if not n:
            return 0, True
        lr, lb = rank_balance(n.left)
        if not lb:
            return lr + 1, False
        rr, rb = rank_balance(n.right)
        return max(lr, rr) + 1, lb and rb and abs(lr - rr) <= 1

    return rank_balance(root)[1]


def identical(a: Node, b: Node) -> bool:
    """Return True if `a` and `b` have identical structure and data."""
    return a == b or bool(
        a
        and b
        and a.data == b.data
        and identical(a.left, b.left)
        and identical(a.right, b.right),
    )


def mirror(r: Node) -> None:
    """Mirror the tree at `r` in place."""
    if r:
        r.left, r.right = r.right, r.left
        mirror(r.left)
        mirror(r.right)


def symmetric(r: Node) -> bool:
    """Return True if tree starting at `r` is symmetric."""

    def sym(a: Node, b: Node) -> bool:
        return a == b or (
            bool(a)
            and bool(b)
            and a.data == b.data
            and sym(a.left, b.right)
            and sym(b.left, a.right)
        )

    return not r or sym(r.left, r.right)


def flat(r: Node) -> bool:
    """Return True if all leaves are at the same level."""
    lvl = [-1]

    def eql(n: Node, cl: int) -> bool:
        if not n:
            return True
        if not n.left and not n.right:
            if lvl[0] == -1:
                lvl[0] = cl
            return cl == lvl[0]
        return eql(n.left, cl + 1) and eql(n.right, cl + 1)

    return eql(r, 0)


def insert(r: Node, value: int) -> Node:
    """Insert `value` into a BST starting at `r`."""
    if not r:
        return TreeNode(value)
    if value < r.data:
        r.left = insert(r.left, value)
    elif value > r.data:
        r.right = insert(r.right, value)
    return r


def find_bst_ancestor(r: Node, a: int, b: int) -> Node:
    """Find lowest common ancestor of `a` and `b` valued nodes in a BST."""
    mn = min(a, b)
    mx = max(a, b)
    while r:
        if r.data > mx:
            r = r.left
        elif r.data < mn:
            r = r.right
        else:
            break
    return r


def lowest_common_ancestor(n: Node, a: int, b: int) -> Node:
    """Find lowest common ancestor of `a` and `b` valued nodes in a tree."""
    if n is None or n.data in (a, b):
        return n
    l = lowest_common_ancestor(n.left, a, b)
    r = lowest_common_ancestor(n.right, a, b)
    return l and r and n or l or r


def no_siblings_nodes(t: Node) -> list:
    """Return nodes' values which have no sibling node from tree `t`."""
    singles = []

    def enum(l: Node, r: Node) -> None:
        if l:
            enum(l.left, l.right)
            if not r:
                singles.append(l.data)
        if r:
            enum(r.left, r.right)
            if not l:
                singles.append(r.data)

    if t:
        enum(t.left, t.right)
    return sorted(singles)


def has_path_sum(n: Node, s: int) -> bool:
    """Return True if there is a path from root `n` to a leaf with sum = `s`."""
    s -= n.data
    return (
        s > 0
        and (n.left and has_path_sum(n.left, s) or n.right and has_path_sum(n.right, s))
        or (s == 0 and not n.left and not n.right)
    )


def count_in_range(n: Node, l: int, h: int) -> int:
    """Count number of nodes form `n` in range (`l`...`h`)."""
    return (
        (
            int(l <= n.data <= h)
            + (count_in_range(n.left, l, h) if n.data > l else 0)
            + (count_in_range(n.right, l, h) if n.data < h else 0)
        )
        if n
        else 0
    )


def median(t: Node) -> float:
    """Return median value for tree starting at `t`."""
    n = sum(1 for _ in ino(t))
    it = islice(ino(t), (n - 1) // 2, None)
    return next(it) if n % 2 else (next(it) + next(it)) / 2


def max_width(t: Node) -> int:
    """Max width at any level in tree `t`."""

    def level_width() -> Iterator:
        q = deque([t])
        while q:
            yield len(q)
            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

    return reduce(max, level_width())


def max_path_sum(t: Node) -> int:
    """Return max path sum between nodes of rank 1."""
    mx = -inf

    def rec(n: Node) -> int:
        nonlocal mx
        if not n:
            return 0
        ls = rec(n.left)
        rs = rec(n.right)
        if (n.left and n.right) or n == t:
            mx = max(mx, n.data + ls + rs)
            return n.data + max(ls, rs)
        return n.data + ls + rs

    rec(t)
    return int(mx)


def to_linked_list(r: Node) -> Node:
    """Transform tree `r` into a double linked list in order."""
    h = t = None
    for n in ino(r, nodes=True):
        h = h or n
        if t:
            t.right = n
        n.left, t = t, n
    if t:
        t.right = None
    return h


def nodes_at_distance(r: Node, target: int, k: int) -> list[int]:
    """Return nodes from tree `r` at distance `k` from `target` node."""
    result = []

    def descend(r: Node, kn: int) -> None:
        if not r or kn < 0:
            return
        if kn == 0:
            result.append(r.data)
            return
        descend(r.left, kn - 1)
        descend(r.right, kn - 1)

    def search(r: Node) -> int | None:
        if not r:
            return None
        if r.data == target:
            descend(r, k)
            return 1
        d = search(r.left)
        if d:
            descend(r.right, k - d - 1)
        else:
            d = search(r.right)
            if d:
                descend(r.left, k - d - 1)
        if k == d:
            result.append(r.data)
            return None
        return d + 1 if d else None

    search(r)
    return sorted(result)


def merge_sorted(r1: Node, r2: Node) -> list:
    """Return a list of sorted values from BST `r1` and `r2`."""
    # Runs in O(M+N) time complexity.
    # Auxiliary space (necessary for the DFO stack):
    #    O(max(|r1|, |r2|)) < O(M+N)
    out = []
    it1 = ino(r1)
    it2 = ino(r2)
    v1 = next(it1, None)
    v2 = next(it2, None)
    while v1 is not None and v2 is not None:
        if v1 < v2:
            out.append(v1)
            v1 = next(it1, None)
        else:
            out.append(v2)
            v2 = next(it2, None)
    if v1 is not None:
        out.append(v1)
        out.extend(it1)
    elif v2 is not None:
        out.append(v2)
        out.extend(it2)
    return out


def tree_distance(root: Node, target: Any) -> int:
    """Return max distance to all nodes from the one with the `target` value."""
    # This puzzle is also known as `burning tree` puzzle.

    def search(r: Any) -> tuple[int, int]:
        if not r:
            return 0, 0

        # Try to find `target`.
        # If not compute the max depth.
        fl, dl = search(r.left)
        fr, dr = search(r.right)
        # return:
        #    path-length since target if found else 0,
        #    max distance to all nodes from the target
        return (
            fl
            and (fl + 1, max(fl + 1 + dr, dl))
            or fr
            and (fr + 1, max(fr + 1 + dl, dr))
            or (int(r.data == target), max(dl, dr) + 1)
        )

    return search(root)[1] - 1


def fix_two_nodes(root: Node) -> None:
    """Given a BST with two nodes swapped fix the tree at `root`."""
    # Swap the two node values in the in-order sequence.
    # E.g.
    #     __10                _10_
    #    /    \              /    \
    #    5_   8        =>    5   20
    #   /  \                / \
    #   2 20                2 8
    #
    #  2, 5, 20, 10, 8 => 2, 5, 8, 10, 20
    #
    a: Node = None  # stores the first anomaly left node
    b: Node = None  # stores the last anomaly right node

    # Uses recursion (stack) for in-order traversal.
    def rec(p: Node, n: Node) -> Node:
        # recursive in-order descend
        # `p` tracks the most recent / previous node.
        nonlocal a, b
        if not n:
            return p
        # left
        p = rec(p, n.left)
        # middle
        if p and p.data > n.data:
            a, b = a or p, n
        # right
        return rec(n, n.right)

    rec(None, root)

    if a and b:
        a.data, b.data = b.data, a.data


def candy_tree_equality(r: TreeNode) -> int:
    """Equalize values in the tree to one. Count minimum number of moves."""
    # Idea is to do it bottom-up.
    # Candy is moved from parent to child if child's candy count is 0.
    # Candy is moved up to the parent if child's candy count is more than 1.
    moves = 0

    def dfs(n: Node) -> int:
        nonlocal moves
        l = dfs(n.left) - 1 if n.left else 0
        r = dfs(n.right) - 1 if n.right else 0

        # Add moves related to the child nodes.
        moves += abs(l) + abs(r)
        # Return candy balance for this node.
        return n.data + l + r

    assert dfs(r) == 1  # noqa: S101
    return moves


def min_bst_with_a_sum(r: Node, target: int) -> int:
    """Find a subtree under `r` that has a sum of nodes equal to `target`.

    Return the count of nodes for a smallest tree like that.

    Parameters
    ----------
    r : Node
        Root node.
    target : int
        Searched sum of nodes for the subtree.

    Returns
    -------
    int
        Count of nodes in the subtree.

    """

    # This solutions bubbles up the node count and
    # the value sum in bottom-up DFS manner.
    # The BST check is done separately.
    def dfs(n: Node) -> tuple[float, int, int]:
        # Returns:
        #    min node count,
        #    current tree node count,
        #    current tree value sum,
        if not n:
            return inf, 0, 0
        lmc, lc, ls = dfs(n.left)
        rmc, rc, rs = dfs(n.right)
        mc = min(lmc, rmc)
        if mc < inf:
            # Cannot get better
            return mc, 0, 0
        c, s = lc + rc + 1, ls + rs + n.data
        if s == target and is_bst(n):
            # Found the target.
            return c, 0, 0
        return inf, c, s

    mc = dfs(r)[0]
    return int(mc) if mc < inf else -1


def min_bst_with_a_sum_single_pass(r: Node, target: int) -> int:
    """Find a subtree under `r` that has a sum of nodes equal to `target`.

    Return the count of nodes for a smallest tree like that.

    Parameters
    ----------
    r : Node
        Root node.
    target : int
        Searched sum of nodes for the subtree.

    Returns
    -------
    int
        Count of nodes in the subtree.

    """

    def dfs(n: Node) -> tuple[float, int, int, float, float]:
        if not n:
            # Return inf min node count and generous interval.
            # mnc, nc, sum, mn, mx
            return inf, 0, 0, inf, -inf
        lmc, lc, ls, lmn, lmx = dfs(n.left)
        rmc, rc, rs, rmn, rmx = dfs(n.right)
        mc = min(lmc, rmc)
        nc = lc + rc + 1
        if mc < inf:
            # We found the min count under this node.
            # mn, nc, sum, mx, mnc
            return mc, 0, 0, 0, 0
        if not lmx < n.data < rmn:
            # This is not a BST.
            # Return inf min node count and prohibitive interval.
            # mnc, nc, sum, mn, mx
            return inf, 0, 0, -inf, inf
        s = ls + rs + n.data
        if s == target:
            # This node is a BST with fitting target sum.
            # mn, nc, sum, mx, mnc
            return nc, 0, 0, 0, 0
        # Propagate info upwards.
        # Handle interval brackets for missing children.
        return inf, nc, s, min(lmn, n.data), max(rmx, n.data)

    mc = dfs(r)[0]
    return int(mc) if mc < inf else -1


def number_of_turns(r: Node, a: int, b: int) -> int:
    """Count number of turns between `a` and `b` in a tree starting at `r`.

    Parameters
    ----------
    r : Node
        Root node of the tree.
    a : int
        First node value.
    b : int
        Second node value.

    Returns
    -------
    int
        Number of turns on the path from `a` to `b`.

    """
    # The idea is to first find the lowest common ancestor.
    # Then to compute the number of turns between `a` and `b`
    # Starting from the `lca`.
    # Finding `lca` makes it easier to calculate the turns.

    def turns(n: Node, target: int, d: str) -> int:
        if n is None:
            return -1
        if n.data == target:
            return 0
        lt = turns(n.left, target, "L")
        if lt >= 0:
            return lt + (d == "R")
        rt = turns(n.right, target, "R")
        if rt >= 0:
            return rt + (d == "L")
        return -1

    if r is None or a == b:
        return -1
    lca = lowest_common_ancestor(r, a, b)
    if lca is None:
        return -1

    return turns(lca, a, "") + turns(lca, b, "") + (lca.data not in (a, b))
