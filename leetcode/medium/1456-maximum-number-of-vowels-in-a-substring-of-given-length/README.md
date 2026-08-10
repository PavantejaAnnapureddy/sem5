# Maximum Number of Vowels in a Substring of Given Length

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s` and an integer `k`, return  *the maximum number of vowel letters in any substring of* `s` *with length* `k`.

 **Vowel letters**  in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

 

 **Example 1:** 

```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

```

 **Example 2:** 

```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

```

 **Example 3:** 

```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of lowercase English letters.
- 1 <= k <= s.length

## Solution

**Language:** Python  
**Runtime:** 47 ms (beats 78.76%)  
**Memory:** 20 MB (beats 11.91%)  
**Submitted:** 2026-08-10T09:46:50.962Z  

```py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        current = 0
        for i in range(k):
            if s[i] in vowels:
                current += 1
        
        max_vowels = current
        
        for i in range(k, len(s)):
        
            if s[i - k] in vowels:
                current -= 1
      
            if s[i] in vowels:
                current += 1
            max_vowels = max(max_vowels, current)
        
        return max_vowels
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)