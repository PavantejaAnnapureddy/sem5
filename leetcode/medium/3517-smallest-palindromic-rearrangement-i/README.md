# Smallest Palindromic Rearrangement I

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a  **palindromic**  string `s`.

Return the  **lexicographically smallest**  palindromic permutation of `s`.

 

 **Example 1:** 

 **Input:**  s = "z"

 **Output:**  "z"

 **Explanation:** 

A string of only one character is already the lexicographically smallest palindrome.

 **Example 2:** 

 **Input:**  s = "babab"

 **Output:**  "abbba"

 **Explanation:** 

Rearranging `"babab"` → `"abbba"` gives the smallest lexicographic palindrome.

 **Example 3:** 

 **Input:**  s = "daccad"

 **Output:**  "acddca"

 **Explanation:** 

Rearranging `"daccad"` → `"acddca"` gives the smallest lexicographic palindrome.

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.
- s is guaranteed to be palindromic.

## Solution

**Language:** Python  
**Runtime:** 151 ms (beats 97.70%)  
**Memory:** 21 MB (beats 51.15%)  
**Submitted:** 2026-07-28T10:17:24.698Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/)