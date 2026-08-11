from collections import Counter

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

        return best