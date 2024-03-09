"Puzzles related to board games."

def queens(n: int) -> list:
    "Return a list of queen combinations for an `NxN` board."
    n4 = n*4
    solutions = []
    s = [0] * n
    def rec(r: int, invalid: int):
        for c in range(n):
            place = (1 << c) + + (1 << (n + c + r)) + (1 << (n4 + c - r))
            if invalid & place:
                continue
            s[r] = c + 1
            if r == 0:
                solutions.append(s[:])
                return
            rec(r-1, invalid | place)
    rec(n-1, 0)
    return sorted(solutions)
