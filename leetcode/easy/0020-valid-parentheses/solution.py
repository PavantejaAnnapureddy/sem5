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