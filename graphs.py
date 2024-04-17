"""Puzzles related to graphs."""

from typing import List, Iterable, Set
from collections import deque

from sequences import find_if
from sets import powerset


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


def topological_order(vertexes: Iterable, edges: dict) -> Iterable:
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
    return len(gr) == len(vis) and all(len(c[0]) == c[1] for c in gr.values())


def articulation_points(adj: List[List[int]]) -> List[int]:
    "Return the articulation points for a graph defined by the `adj` list."
    # This uses single pass Tarjan's Algorithm.
    vt = [0] * len(adj)  # visited time for each node in DFS-tree order
    ct = vt[:]  # circle time for the parent/root of the whole circle
    o = []

    # Depth first search to determine the parent of each node
    # and created the DFS-tree.
    def dfs(p, n, t):
        vt[n] = ct[n] = t  # set the times
        # art - boolean indicating if `n` is an articulate point.
        # kids - number of kids reached from this node first.
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
                # Use the original visited time, given that
                # the child may be in another circle.
                ct[n] = min(ct[n], vt[c])
        # Append the node if it is marked as an articulate point.
        # For the root of the DFS-tree (p == -1), we just need
        # to check if there are more than two kids (not in the same circle).
        if art if p != -1 else kids > 1:
            o.append(n)

    # Start search from the first node (== 0).
    dfs(-1, 0, 1)
    return sorted(o)


def critical_connections(adj: List[List[int]]) -> List[List[int]]:
    "Return a list of critical bridges in an unordered graph."
    # This uses single pass Tarjan's Algorithm.
    vt = [0] * len(adj)  # visited time for each node in DFS-tree order
    ct = vt[:]  # circle time for the parent/root of the whole circle
    o = set()

    # Depth first search to determine the parent of each node
    # and created the DFS-tree.
    def dfs(p, n, t):
        vt[n] = ct[n] = t  # set the times
        for c in adj[n]:
            if not vt[c]:  # If the child node was not visited...
                dfs(n, c, t + 1)
                # If the child circle time is lower than ours,
                # it has reached another node up in the DFT-tree.
                # This indicates that we are in a circle with the child.
                ct[n] = min(ct[n], ct[c])
                # If the child is in a circle later than our visit time,
                # this means that child can only be visited through this node.
                if ct[c] > t:
                    o.add((n, c))
            elif c != p:  # visited node before
                # If we reached another node (but the parent) higher
                # in the DFS-tree, update our circle time.
                # Use the original visited time, given that
                # the child may be in another circle.
                ct[n] = min(ct[n], vt[c])

    # Start search from the first node (== 0).
    dfs(-1, 0, 1)
    return sorted(o)


def vertex_cover_optimal(edges: List[List[int]]) -> Set[int]:
    "Return the vertices of a minimal vertex cover."
    edges_ = list(map(set, edges))  # Make edges undirected and easy to intersect.
    vertexes = set.union(*edges_)  # Limit to interesting vertexes.
    covers_all_edges = lambda s: all(e & s for e in edges_)
    return find_if(covers_all_edges, powerset(vertexes)) or vertexes


def word_distance(words: Iterable[str], start: str, end: str) -> int:
    "Return the minimum distance from `start` to `end` when using `words` intermediate steps."
    # The idea is to use breadth first search BFS and keep track of the depth.
    # The first time we hit the target end word, we return the depth calculated so far.
    if start == end:
        return 1
    lookup = set(words)
    q = deque([start])
    depth = 2  # `start` and `end` are two words
    while q:
        # Standard BFS level expansion based on current queue length.
        for _ in range(len(q)):
            word = q.popleft()
            # Generate the neighbors by manipulating the string.
            for i in range(len(word)):
                for rc in "abcdefghijklmnopqrstuvwxyz":
                    # String manipulation and string set lookup are faster than
                    # converting to a list and back to a hashable object.
                    nw = word[:i] + rc + word[i + 1 :]
                    if nw == end:
                        return depth
                    if nw in lookup:
                        # Avoid cycles and mark visited nodes.
                        lookup.remove(nw)
                        q.append(nw)
        depth += 1
    return 0


def word_paths(words: Iterable[str], start: str, end: str) -> List[List[str]]:
    "Return the minimum paths from `start` to `end` when using `words` intermediate steps."
    # The idea is to treat the words list as an adjacency list of a graph
    # While traversing the, the set of adjacent words is reduced to keep track of
    # visited nodes in breadth first search (BFS) and to remove any cycles.
    # BFS will provide the shortest paths if aborted after the target end word is found.
    # A queue is used to keep paths found so far.
    #
    # Current set of yet to be visited nodes in the graph.
    lookup = set(words)
    # The queue contains paths as Python lists.
    q = deque([[start]])
    # Keep track of the goal. Abort at the earliest hit.
    found = start == end
    # Using BFS while tracking the paths.
    while q and not found:
        # Track the visited nodes (words) in the BFS expansion.
        used = set()
        # Standard BFS level expansion based on current queue length.
        for _ in range(len(q)):
            path = q.popleft()
            word = path[-1]
            # Generate the neighbors by manipulating the string.
            for i in range(len(word)):
                for rc in "abcdefghijklmnopqrstuvwxyz":
                    # String manipulation and string set lookup are faster than
                    # converting to a list and back to a hashable object.
                    nw = word[:i] + rc + word[i + 1 :]
                    if nw in lookup:
                        # Keeping track of "used" words as set is faster.
                        used.add(nw)
                        # Extending the path is faster than any other manipulations.
                        q.append(path + [nw])
                    # Terminate if found.
                    found |= nw == end
        # We can remove the used words after a level of BFS.
        # This allows us to add multiple paths, even those share some words.
        lookup -= used
    # Filter the last level to only the paths ending in the target word.
    return [p for p in q if p[-1] == end]
