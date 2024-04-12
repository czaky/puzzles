"""Puzzles related to binary (search) trees."""

import math
from collections import deque
from typing import Tuple, Optional, List, Deque
from itertools import islice
from functools import reduce


class TreeNode:
    "Node of a binary tree."

    def __init__(self, data):
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.height: int = 1

    def __iter__(self):
        # level order (breadth first)
        r: Node = self
        q = deque([r])
        while q:
            n = q.popleft()
            yield n.data
            n.left and q.append(n.left)
            n.right and q.append(n.right)

    def inorder(self):
        "In-order iterator."
        if self.left:
            yield from self.left.inorder()
        yield self.data
        if self.right:
            yield from self.right.inorder()

    def display(self, v=False):
        "Display the tree in a visual 2D manner."

        def aux(node):
            "-> lines, width, height, middle"
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
                return [first, second] + shifted, n + u, p + 2, n + u // 2

            # Only right child.
            if not node.left:
                lines, n, p, x = aux(node.right)
                first = s + x * "_" + (n - x) * " "
                second = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted = [u * " " + line for line in lines]
                return [first, second] + shifted, n + u, p + 2, u // 2

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
            print(line)

        if v:
            print("-" * mxl)
            print(self.bfo_string())
            print("-" * mxl)

    def bfo_string(self, none: str = "N") -> str:
        "Return a BFO string representation using none ('N') for None."
        o = []
        q: Deque[Node] = deque([self])
        while q:
            n = q.popleft()
            o.append(str(n.data) if n else none)
            if n:
                q.append(n.left)
                q.append(n.right)
        while o and o[-1] == none:
            o.pop()
        return " ".join(o)

    def update_height(self):
        "Update the height of this node based on its children."
        self.height = 1 + max(height(self.left), height(self.right))

    def left_rotate(self) -> "TreeNode":
        "Rotate the tree at this node to the left."
        #  2_         _4
        # /  \       /  \
        # 1  4   =>  2  5
        #   / \     / \
        #   3 5     1 3
        assert self.right
        y = self.right
        self.right = y.left
        y.left = self
        # Update the height of this (lower) node first.
        self.update_height()
        y.update_height()
        return y

    def right_rotate(self) -> "TreeNode":
        "Rotate the tree at this node to the right."
        #   _4         2_
        #  /  \       /  \
        #  2  5   =>  1  4
        # / \           / \
        # 1 3           3 5
        assert self.left
        y = self.left
        self.left = y.right
        y.right = self
        # Update the height of this (lower) node first.
        self.update_height()
        y.update_height()
        return y

    def left_skew(self) -> int:
        "Return how far to the left the node is skewed."
        l, r = self.left, self.right
        return (l and l.height or 0) - (r and r.height or 0)

    def balance_node(self) -> "TreeNode":
        "Balance this node. May return one of its descendants."

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

    def insert_balanced(self, value: int):
        "Insert a node with `value`"
        if value < self.data:
            self.left = insert_balanced(self.left, value)
        elif value > self.data:
            self.right = insert_balanced(self.right, value)
        else:
            return self

        return self.balance_node()

    def delete_balanced(self, value: int):
        "Delete the `value` from a self-balancing AVL tree."
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
    "Return the height of a Node `n` or 0 for NONE."
    return n and n.height or 0


def make(s: str, none: str = "N") -> Node:
    "Make a binary tree from a string `s` in breadth first order."
    it = iter(s.split())
    v = next(it, none)
    if v == none:
        return None
    root = TreeNode(int(v))
    q = deque([root])
    for v in it:
        n = q.popleft()
        if v != none:
            n.left = TreeNode(int(v))
            q.append(n.left)
        v = next(it, None)
        if v is None:
            break
        if v != none:
            n.right = TreeNode(int(v))
            q.append(n.right)
    for n in df_nodes(root):
        n.update_height()
    return root


def make_df(s: str, none: str = "N") -> Node:
    "Make a binary tree from a string `s` in depth first order."

    def des(it):
        v = next(it, none)
        if v == none:
            return None
        n = TreeNode(int(v))
        n.left = des(it)
        n.right = des(it)
        n.update_height()
        return n

    return des(iter(s.split()))


def insert_balanced(n: Node, value: int):
    "Insert a node with `value`"
    return n.insert_balanced(value) if n else TreeNode(value)


# Determine if a tree is an ordered BST (may be unbalanced)
def is_bst(root: Node) -> bool:
    "True if `root` is a BST."

    def ordered(n: Node, mn: float, mx: float) -> bool:
        return not n or (
            (mn <= n.data <= mx)
            and ordered(n.left, mn, n.data - 1)
            and ordered(n.right, n.data + 1, mx)
        )

    return ordered(root, -math.inf, math.inf)


def left_view(root: Node) -> list:
    "Return the projected left view of the binary tree from `root`."
    view = []

    def enum(n: Node, level: int):
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.left, level + 1)
        enum(n.right, level + 1)

    enum(root, 1)
    return view


def right_view(root: Node) -> list:
    "Return the projected right view of the binary tree from `root`."
    view = []

    def enum(n: Node, level: int):
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.right, level + 1)
        enum(n.left, level + 1)

    enum(root, 1)
    return view


def bfo(t: Node):
    "Yield node values in breadth first order."
    q = deque([t])
    while q:
        n = q.popleft()
        yield n.data
        n.left and q.append(n.left)
        n.right and q.append(n.right)


def breadth_first(t: Node) -> list:
    """Return the node values in breadth first order."""
    return list(bfo(t))


def reversed_level_order(t: Node) -> list:
    "Return reversed breadth first (level order) enumeration."
    q = deque([t])
    r = []
    while q:
        n = q.popleft()
        r.append(n.data)
        # append right first
        n.right and q.append(n.right)
        n.left and q.append(n.left)
    return list(reversed(r))


def dfo(c: Node):
    "Yield node values in depth first order."
    s = []
    while s or c:
        while c:
            s.append(c)
            c = c.left
        c = s.pop()
        yield c.data
        c = c.right


def df_nodes(c: Node):
    "Yield nodes in depth first order."
    s = []
    while s or c:
        while c:
            s.append(c)
            c = c.left
        c = s.pop()
        yield c
        c = c.right


def depth_first(t: Node) -> list:
    """Return the node values in depth first order."""
    return list(dfo(t))


def successor(t: Node, x: int) -> Optional[Node]:
    "Return the successor Node in `t` for value `x` in order enumeration."
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
    "Return k-largest element from a BST at `r`."
    # Depth First Search on the right side.
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


def spiral_order(t: Node) -> list:
    """
    Return the node values in spiral.
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
            n.left and q.append(n.left)
            n.right and q.append(n.right)
        o.extend(reversed(ro))
    return o


def balanced(root: Node) -> bool:
    "True if tree at `root` is balanced in height."

    def rank_balance(n: Node) -> Tuple[int, bool]:
        if not n:
            return 0, True
        lr, lb = rank_balance(n.left)
        if not lb:
            return lr + 1, False
        rr, rb = rank_balance(n.right)
        return max(lr, rr) + 1, lb and rb and abs(lr - rr) <= 1

    return rank_balance(root)[1]


def identical(a: Node, b: Node) -> bool:
    "True if `a` and `b` have identical structure and data."
    return a == b or bool(
        a
        and b
        and a.data == b.data
        and identical(a.left, b.left)
        and identical(a.right, b.right)
    )


def mirror(r: Node):
    "Mirror the tree at `r` in place."
    if r:
        r.left, r.right = r.right, r.left
        mirror(r.left)
        mirror(r.right)


def symmetric(r: Node) -> bool:
    "True if tree starting at `r` is symmetric."

    def sym(a, b):
        return a == b or (
            a
            and b
            and a.data == b.data
            and sym(a.left, b.right)
            and sym(b.left, a.right)
        )

    return bool(not r or sym(r.left, r.right))


def flat(r: Node) -> bool:
    "True if all leaves are at the same level."
    lvl = [-1]

    def eql(n, cl):
        if not n:
            return True
        if not n.left and not n.right:
            if lvl[0] == -1:
                lvl[0] = cl
            return cl == lvl[0]
        return eql(n.left, cl + 1) and eql(n.right, cl + 1)

    return eql(r, 0)


def insert(r: Node, value: int) -> Node:
    "Insert `value` into a BST starting at `r`."
    if not r:
        return TreeNode(value)
    if value < r.data:
        r.left = insert(r.left, value)
    elif value > r.data:
        r.right = insert(r.right, value)
    return r


def find_ancestor(r: Node, a: int, b: int) -> Optional[Node]:
    "Find lowest common ancestor of `a` and `b` valued nodes."
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


def no_siblings_nodes(t: Node) -> list:
    "Return nodes' values which have no sibling node from tree `t`."
    singles = []

    def enum(l, r):
        l and (enum(l.left, l.right), r or singles.append(l.data))
        r and (enum(r.left, r.right), l or singles.append(r.data))

    t and enum(t.left, t.right)
    return sorted(singles)


def has_path_sum(n: Node, s: int) -> bool:
    "True if there is a path from root `n` to a leaf with sum = `s`."
    s -= n.data
    return (
        s > 0
        and (n.left and has_path_sum(n.left, s) or n.right and has_path_sum(n.right, s))
        or (s == 0 and not n.left and not n.right)
    )


def count_in_range(n: Node, l: int, h: int) -> int:
    "Count number of nodes form `n` in range (`l`...`h`)."
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
    "Return median value for tree starting at `t`."
    n = sum(1 for _ in dfo(t))
    it = islice(dfo(t), (n - 1) // 2, None)
    return next(it) if n % 2 else (next(it) + next(it)) / 2


def max_width(t: Node) -> int:
    "Max width at any level in tree `t`."

    def level_width():
        q = deque([t])
        while q:
            yield len(q)
            for _ in range(len(q)):
                n = q.popleft()
                n.left and q.append(n.left)
                n.right and q.append(n.right)

    return reduce(max, level_width())


def max_path_sum(t: Node) -> int:
    "Return max path sum between nodes of rank 1."
    mx = [-math.inf]

    def rec(n):
        if not n:
            return 0
        ls = rec(n.left)
        rs = rec(n.right)
        if (n.left and n.right) or n == t:
            mx[0] = max(mx[0], n.data + ls + rs)
            return n.data + max(ls, rs)
        return n.data + ls + rs

    rec(t)
    return int(mx[0])


def to_linked_list(r: Node) -> Node:
    "Transform tree `r` into a double linked list in order."
    h = t = None
    for n in df_nodes(r):
        h = h or n
        if t:
            t.right = n
        n.left, t = t, n
    if t:
        t.right = None
    return h


def nodes_at_distance(r: Node, target: int, k: int) -> List[int]:
    "Return nodes from tree `r` at distance `k` from `target` node."
    result = []

    def descend(r: Node, kn: int):
        if not r or kn < 0:
            return
        if kn == 0:
            result.append(r.data)
            return
        descend(r.left, kn - 1)
        descend(r.right, kn - 1)

    def search(r: Node):
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
    "Return a list of sorted values from BST `r1` and `r2`."
    # Runs in O(M+N) time complexity.
    # Auxiliary space (necessary for the DFO stack):
    #    O(max(|r1|, |r2|)) < O(M+N)
    out = []
    it1 = dfo(r1)
    it2 = dfo(r2)
    v1 = next(it1, None)
    v2 = next(it2, None)
    while v1 is not None and v2 is not None:
        if v1 < v2:
            out.append(v1)
            v1 = next(it1, None)
        else:
            out.append(v2)
            v2 = next(it2, None)
    v1 is not None and (out.append(v1), out.extend(it1))
    v2 is not None and (out.append(v2), out.extend(it2))
    return out


def tree_distance(root: Node, target) -> int:
    "Return max distance to all nodes from the one with the `target` value."
    # This puzzle is also known as `burning tree` puzzle.

    def search(r):
        if not r:
            return 0, 0

        # Try to find `target`.
        # If not compute the max depth.
        fl, dl = search(r.left)
        fr, dr = search(r.right)
        return (
            fl
            and (fl + 1, max(fl + 1 + dr, dl))
            or fr
            and (fr + 1, max(fr + 1 + dl, dr))
            or (int(r.data == target), max(dl, dr) + 1)
        )

    return search(root)[1] - 1


def fix_two_nodes(root: Node):
    "Given a BST with two nodes swapped fix the tree at `root`."
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
    def rec(p: Node, n: Node):
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


def candy_tree_equality(r: Node) -> int:
    "Equalize values in the tree to one. Count minimum number of moves."
    # Idea is to do it bottom-up.
    # Candy is moved from parent to child if child's candy count is 0.
    # Candy is moved up to the parent if child's candy count is more than 1.
    moves = 0

    def dfs(n) -> int:
        nonlocal moves
        l = dfs(n.left) - 1 if n.left else 0
        r = dfs(n.right) - 1 if n.right else 0

        # Add moves related to the child nodes.
        moves += abs(l) + abs(r)
        # Return candy balance for this node.
        return n.data + l + r

    assert r and dfs(r) == 1
    return moves
