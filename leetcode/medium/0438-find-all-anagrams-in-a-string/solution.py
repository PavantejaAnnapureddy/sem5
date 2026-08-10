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