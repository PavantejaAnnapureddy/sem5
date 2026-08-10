class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for c in s:
            if c in odd: odd.remove(c)
            else: odd.add(c)
        return len(s) - len(odd) + 1 if odd else len(s)