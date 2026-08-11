class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()  
        left = 0
        best = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            best = max(best, right - left + 1)

        return best

#from collections import Counter
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = Counter()   
        left = 0
        best = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            while window[ch] > 1:
                window[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best"""