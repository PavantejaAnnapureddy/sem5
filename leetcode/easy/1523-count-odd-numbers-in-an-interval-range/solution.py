class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count odds up to high, subtract odds up to low-1
        return (high + 1) // 2 - low // 2