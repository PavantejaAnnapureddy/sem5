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