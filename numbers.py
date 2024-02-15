"""Module for number and arithmetic related puzzles."""

def floor_sqrt(x: int) -> int:
    "Return the floor of `sqrt(x)`."
    if x in (0, 1):
        return x
    l = 0
    h = x
    r = 0
    while l <= h:
        m = (l + h) // 2
        if m*m == x:
            return m
        if m*m < x:
            r = m
            l = m + 1
        else:
            h = m - 1
    return r
