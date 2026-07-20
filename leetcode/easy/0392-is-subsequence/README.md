# Is Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` *if* `s` *is a  **subsequence**  of* `t` *, or* `false` *otherwise*.

A  **subsequence**  of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

 

 **Example 1:** 

```
Input: s = "abc", t = "ahbgdc"
Output: true

```

 **Example 2:** 

```
Input: s = "axc", t = "ahbgdc"
Output: false

```

 

 **Constraints:** 

- 0 <= s.length <= 100
- 0 <= t.length <= 104
- s and t consist only of lowercase English letters.

 

 **Follow up:**  Suppose there are lots of incoming `s`, say `s1, s2,..., sk` where `k >= 109`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 25.04%)  
**Submitted:** 2026-07-20T09:51:52.793Z  

```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
```

---

[View on LeetCode](https://leetcode.com/problems/is-subsequence/)