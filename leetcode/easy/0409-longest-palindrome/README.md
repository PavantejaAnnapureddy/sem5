# Longest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` which consists of lowercase or uppercase letters, return the length of the  **longest palindrome**  that can be built with those letters.

Letters are  **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

 **Example 1:** 

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

 **Example 2:** 

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 53.55%)  
**Memory:** 19.4 MB (beats 28.18%)  
**Submitted:** 2026-08-10T10:25:18.109Z  

```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for c in s:
            if c in odd: odd.remove(c)
            else: odd.add(c)
        return len(s) - len(odd) + 1 if odd else len(s)
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindrome/)