# Smallest Palindromic Rearrangement II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a  **palindromic**  string `s` and an integer `k`.

Return the  **k-th**   **lexicographically smallest**  palindromic permutation of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

 **Note:**  Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 

 **Example 1:** 

 **Input:**  s = "abba", k = 2

 **Output:**  "baab"

 **Explanation:** 

- The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
- Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".

 **Example 2:** 

 **Input:**  s = "aa", k = 2

 **Output:**  ""

 **Explanation:** 

- There is only one palindromic rearrangement: "aa".
- The output is an empty string since k = 2 exceeds the number of possible rearrangements.

 **Example 3:** 

 **Input:**  s = "bacab", k = 1

 **Output:**  "abcba"

 **Explanation:** 

- The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
- Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of lowercase English letters.
- s is guaranteed to be palindromic.
- 1 <= k <= 106

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.6 MB  
**Submitted:** 2026-07-29T10:05:42.048Z  

```py
from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Count frequencies
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        
        # Build half and find middle
        middle = ''
        half = []
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + 97)
            half.extend([chr(i + 97)] * (freq[i] // 2))
        
        half_len = len(half)
        
        # Precompute factorials
        fact = [1] * (half_len + 1)
        for i in range(1, half_len + 1):
            fact[i] = fact[i-1] * i
        
        # Count distinct permutations
        counter = Counter(half)
        
        # Quick check if k is valid
        total = fact[half_len]
        for cnt in counter.values():
            total //= fact[cnt]
        
        if k > total:
            return ""
        
        # Build answer
        result = []
        remaining = k - 1
        
        for pos in range(half_len):
            remaining_positions = half_len - pos - 1
            
            for i in range(26):
                ch = chr(i + 97)
                if counter.get(ch, 0) == 0:
                    continue
                
                counter[ch] -= 1
                
                # Calculate permutations efficiently
                perms = fact[remaining_positions]
                for cnt in counter.values():
                    if cnt > 1:
                        perms //= fact[cnt]
                
                if remaining < perms:
                    result.append(ch)
                    break
                else:
                    remaining -= perms
                    counter[ch] += 1
        
        # Build palindrome
        first = ''.join(result)
        return first + middle + first[::-1] if middle else first + first[::-1]
```

---

[View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)