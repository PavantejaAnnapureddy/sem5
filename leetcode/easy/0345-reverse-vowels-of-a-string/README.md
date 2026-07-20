# Reverse Vowels of a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

 **Example 1:** 

 **Input:**  s = "IceCreAm"

 **Output:**  "AceCreIm"

 **Explanation:** 

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

 **Example 2:** 

 **Input:**  s = "leetcode"

 **Output:**  "leotcede"

 

 **Constraints:** 

- 1 <= s.length <= 3 * 105
- s consist of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 59.81%)  
**Memory:** 20.6 MB (beats 27.07%)  
**Submitted:** 2026-07-20T09:29:37.182Z  

```py
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set('aeiouAEIOU')
        left = 0
        right = len(s_list) - 1
        
        while left < right:
    
            while left < right and s_list[left] not in vowels:
                left += 1
            while left < right and s_list[right] not in vowels:
                right -= 1
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
    
        return ''.join(s_list)
        
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)