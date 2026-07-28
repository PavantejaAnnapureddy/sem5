from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        first = []
        middle = ""
        
        for c in sorted(freq):
            if freq[c] % 2:
                middle = c
            first.append(c * (freq[c] // 2))
        
        first = "".join(first)
        return first + middle + first[::-1]