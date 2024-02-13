# Puzzles related to strings.abs

def reverse_words(s: str, sep: str=' ') -> str:
    "Reverse the order of words in `s`, separated by `sep`."
    return sep.join(reversed(s.split(sep)))

def palindrome(s: str) -> bool:
    "True if `s` is a palindrome."
    # s == s[::-1]
    # Runs in O(N) time and O(1) space.
    return next((False for i in range(len(s)//2) if s[i] !=s [-1-i]), True)