class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        def dist(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)
        
        best = float('inf')
        
        for k in range(n):
            cost_rot = k
            cost_pairs = 0
            for i in range(n // 2):
                left = (k + i) % n
                right = (k + n - 1 - i) % n
                cost_pairs += dist(s[left], s[right])
            best = min(best, cost_rot + cost_pairs)
        
        return best