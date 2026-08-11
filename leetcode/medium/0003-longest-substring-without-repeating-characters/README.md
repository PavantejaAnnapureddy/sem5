# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 105
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 216 ms (beats 14.88%)  
**Memory:** 19.9 MB (beats 8.88%)  
**Submitted:** 2026-08-11T10:17:14.942Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)