# Find All Anagrams in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```

 **Example 2:** 

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

```

 

 **Constraints:** 

- 1 <= s.length, p.length <= 3 * 104
- s and p consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 31 ms (beats 80.59%)  
**Memory:** 19.9 MB (beats 15.78%)  
**Submitted:** 2026-08-10T09:54:49.515Z  

```py
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        count = [0] * 26
        for c in p:
            count[ord(c) - 97] += 1
        
        result = []
        left = 0
        
        for right in range(len(s)):
            count[ord(s[right]) - 97] -= 1
            
            while count[ord(s[right]) - 97] < 0:
                count[ord(s[left]) - 97] += 1
                left += 1
            
            if right - left + 1 == len(p):
                result.append(left)
        
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)