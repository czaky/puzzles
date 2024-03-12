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
    # build graph
    gr = {}
    for w in words:
        (gr.get(w[0]) or gr.setdefault(w[0], [[], 0]))[0].append(w[-1])
        (gr.get(w[-1]) or gr.setdefault(w[-1], [[], 0]))[1] += 1
    # connectivity check
    vis = set()
    dfs = lambda c: c in vis or vis.add(c) or all(map(dfs, gr[c][0]))
    dfs(words[0][0])
    # connectivity and vertex degree check
    return int(len(gr) == len(vis) and all(len(c[0]) == c[1] for c in gr.values()))
