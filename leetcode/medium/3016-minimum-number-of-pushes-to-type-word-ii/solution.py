class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freq):
            pushes_needed = (i // 8) + 1
            total_pushes += count * pushes_needed
        
        return total_pushes