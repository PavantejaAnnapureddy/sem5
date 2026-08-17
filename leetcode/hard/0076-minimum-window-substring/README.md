# Minimum Window Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return  *the  **minimum window***   ***substring**  **of  *`s`*  such that every character in  *`t`*  (** including duplicates**) is included in the window *. If there is no such substring, return* the empty string *`""`.

The testcases will be generated such that the answer is  **unique**.

 

 **Example 1:** 

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

```

 **Example 2:** 

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

```

 **Example 3:** 

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

```

 

 **Constraints:** 

- m == s.length
- n == t.length
- 1 <= m, n <= 105
- s and t consist of uppercase and lowercase English letters.

 

 **Follow up:**  Could you find an algorithm that runs in `O(m + n)` time?

## Solution

**Language:** Python  
**Runtime:** 122 ms (beats 32.36%)  
**Memory:** 19.6 MB (beats 94.29%)  
**Submitted:** 2026-08-17T06:08:34.720Z  

```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = {}
        required = len(need)
        formed = 0
        left = 0
        min_len = float('inf')
        result = ""
        
        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1
            
            if c in need and have[c] == need[c]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                
                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-window-substring/)