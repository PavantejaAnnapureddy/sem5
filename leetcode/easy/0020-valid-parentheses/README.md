# Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

 

 **Example 1:** 

 **Input:**  s = "()"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "()[]{}"

 **Output:**  true

 **Example 3:** 

 **Input:**  s = "(]"

 **Output:**  false

 **Example 4:** 

 **Input:**  s = "([])"

 **Output:**  true

 **Example 5:** 

 **Input:**  s = "([)]"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 44.86%)  
**Memory:** 19.3 MB (beats 63.33%)  
**Submitted:** 2026-08-06T17:34:17.684Z  

```py
class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(char)
        
        # If stack is empty, all brackets matched correctly
        return not stack
```

---

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)