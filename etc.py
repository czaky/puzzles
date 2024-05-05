"""Module for algorithms and puzzles that do not fit to other categories."""

from __future__ import annotations

from functools import lru_cache


def fruit_pickup_min_time(locations: list[int], types: list[int]) -> int:
    """Given an array of `locations` and fruit `types`, compute the shortest
    path to pickup fruits starting at lowest type up to the hightest.

    `locations` and `types` have the same length.

    Args:
    ----
        locations (List[int]): locations of the fruits
        types (List[int]): type of the fruit

    Returns:
    -------
        int: minimum number of steps to pickup the fruits.

    """
    tl: dict[int, list[int]] = {0: [0, 0], (max(types) + 1): [0, 0]}
    for t, loc in zip(types, locations):
        tnl, txl = tl.get(t) or tl.setdefault(t, [loc, loc])
        tl[t][:] = min(loc, tnl), max(loc, txl)
    tsort = [tl[i] for i in sorted(tl)]
    pick = [0, 0]
    for i in range(1, len(tsort)):
        mn, mx = tsort[i - 1]
        pl, pr = pick
        for lr in (0, 1):
            np = tsort[i][lr]
            if mx <= np:
                # mn ... mx <= pp
                # move all the way left (=0) to mn
                pick[lr] = np - mn + pl
            elif np <= mn:
                # pp <= mn ... mx
                # move all the way right (=1) to mx
                pick[lr] = mx - np + pr
            else:
                # mn, pp, mx
                # opt1: move to mx then to mn (= 0)
                # opt2: move to mn then to mx (= 1)
                pick[lr] = min(mx - np + pl, np - mn + pr) + (mx - mn)
    return min(pick)


def fruit_pickup_min_time_recursive(locs: list[int], types: list[int]) -> int:
    """Given an array of `locations` and fruit `types`, compute the shortest
    path to pickup fruits starting at lowest type up to the hightest.

    `locations` and `types` have the same length.

    Args:
    ----
        locations (List[int]): locations of the fruits
        types (List[int]): type of the fruit

    Returns:
    -------
        int: minimum number of steps to pickup the fruits.

    """
    tl = {}
    for i, loc in enumerate(locs):
        t = types[i]
        tnl, txl = tl.get(t, (loc, loc))
        tl[t] = (min(loc, tnl), max(loc, txl))
    tsort = [(0, 0)] + [tl[i] for i in sorted(tl)] + [(0, 0)]
    n = len(tsort)

    @lru_cache(None)
    def pick(i: int, lr: int):
        if i == n:
            return 0
        pp = tsort[i - 1][lr]
        mn, mx = tsort[i]
        if mx <= pp:
            # mn ... mx , pp
            # move all the way left (=0) to mn
            return pp - mn + pick(i + 1, 0)
        if pp <= mn:
            # pp, mn ... mx
            # move all the way right (=1) to mx
            return mx - pp + pick(i + 1, 1)

        # mn, pp, mx
        # move to mx then to mn (= 0)
        opt1 = (mx - pp) + pick(i + 1, 0)
        # move to mn then to mx (= 1)
        opt2 = (pp - mn) + pick(i + 1, 1)
        return min(opt1, opt2) + (mx - mn)

    return min(pick(1, 0), pick(1, 1))
