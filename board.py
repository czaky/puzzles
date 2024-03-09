"Puzzles related to board games."

def queens(n: int) -> list:
    "Return a list of queen combinations for an `NxN` board."
    solutions = []
    s = [0] * n
    def rec(r: int, invalid: int):
        if r >= n:
            solutions.append(s[:])
            return
        place = 1 | 1 << (n+r) | 1 << (n*4-r)
        for s[r] in range(1, n+1):
            _ = invalid & place or rec(r+1, invalid | place)
            place <<= 1
    rec(0, 0)
    return solutions
