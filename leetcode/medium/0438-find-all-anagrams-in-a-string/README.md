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
**Runtime:** 187 ms (beats 24.52%)  
**Memory:** 19.7 MB (beats 69.06%)  
**Submitted:** 2026-08-10T10:30:07.615Z  

```py
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        p_count = Counter(p)
        s_count = Counter(s[:len(p)])
        result = []
        
        if s_count == p_count:
            result.append(0)
        
        for i in range(len(p), len(s)):
    
            s_count[s[i]] += 1
       
            s_count[s[i - len(p)]] -= 1
            
          
            if s_count[s[i - len(p)]] == 0:
                del s_count[s[i - len(p)]]
            
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)