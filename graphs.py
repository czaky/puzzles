"""Puzzles related to graphs."""

from typing import List, Iterable
from collections import deque


def breadth_first(adj: List[List[int]], start: int = 0) -> List[int]:
    "Traverse the graph breadth first. Return list of nodes."
    q = deque([start])
    v = set([start])
    o = []
    while q:
        n = q.popleft()
        o.append(n)
        for d in adj[n]:
            if not d in v:
                q.append(d)
                v.add(d)
    return o


def depth_first(adj: List[List[int]], start: int = 0) -> List[int]:
    "Traverse the graph depth first using stack. Return list of nodes."
    o = []
    v = set()
    s = [start]
    while s:
        n = s.pop()
        if n not in v:
            v.add(n)
            o.append(n)
            s.extend(filter(lambda a: a not in v, reversed(adj[n])))
    return o


def depth_first_r(adj: List[List[int]], start: int = 0) -> List[int]:
    "Traverse the graph recursively depth first. Return list of nodes."
    o = []
    v = set()

    def dfs(n: int):
        v.add(n)
        o.append(n)
        for a in adj[n]:
            if not a in v:
                dfs(a)

    dfs(start)
    return o


def topological_order(vertexes: list, edges: dict) -> Iterable:
    "Return `vertexes` in topological order based on `edges` relation."
    s = []
    v = set()

    def sort(n):
        if not n in v:
            v.add(n)
            any(map(sort, edges.get(n, [])))
            s.append(n)

    any(map(sort, vertexes))
    return reversed(s)


def circle_of_words(words: List[str]) -> bool:
    "True if `words` can make a circle if connected by the same letter."
    # Euler circle problem.
    #   Words are edges.
    #   Number of inbound and outbound edges need to be equal.
    #   Graph needs to be connected.
    # build graph
    gr = {}
    for w in words:
        # outbound edges
        (gr.get(w[0]) or gr.setdefault(w[0], [[], 0]))[0].append(w[-1])
        # inbound count
        (gr.get(w[-1]) or gr.setdefault(w[-1], [[], 0]))[1] += 1
    # connectivity check
    vis = set()
    (dfs := lambda c: c in vis or vis.add(c) or all(map(dfs, gr[c][0])))(words[0][0])
    # connectivity and vertex degree check
    return int(len(gr) == len(vis) and all(len(c[0]) == c[1] for c in gr.values()))


def articulation_points(adj: List[int]) -> List[int]:
    "Return the articulation points for a graph defined by the `adj` list."
    vt = [0] * len(adj)  # visited time for each node in DFS-tree order
    ct = vt[:]  # circle time for the parent/root of the whole circle
    o = []

    # Depth first search to determine the parent of each node
    # and created the DFS-tree.
    def dfs(p, n, t):
        vt[n] = ct[n] = t  # set the times
        art = kids = 0
        for c in adj[n]:
            if not vt[c]:  # If the child node was not visited...
                dfs(n, c, t + 1)
                # Count the kids of this parent
                # which were not visited earlier by the DFS.
                kids += 1
                # If the child has a higher circle time,
                # that means that this node is not in its circle
                # and thus the child is connected only through this node.
                art |= ct[c] >= t
                # If the child circle time is lower than ours,
                # it has reached another node up in the DFT-tree.
                # This indicates that we are in a circle with the child.
                ct[n] = min(ct[n], ct[c])
            elif c != p:
                # If we reached another node (but the parent) higher
                # in the DFS-tree, update our circle time.
                ct[n] = min(ct[n], vt[c])
        # Append the node if it is marked as an articulate point.
        # For the root of the DFS-tree (p == -1), we just need
        # to check if there are more than two kids (not in the same circle).
        (art if p != -1 else kids > 1) and o.append(n)

    # Start search from the first node (== 0).
    dfs(-1, 0, 1)
    return sorted(o)
