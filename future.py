"Feature Python compatibility."

from itertools import tee


# Python 3.10
def pairwise(iterable):
    "pairwise('ABCDEFG') --> AB BC CD DE EF FG"
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
