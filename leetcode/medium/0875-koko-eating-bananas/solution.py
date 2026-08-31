from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
                if hours > h:
                    return False
            return True
        total = sum(piles)
        left = (total + h - 1) // h  
        right = max(piles)  
        while left < right:
            mid = (left + right) // 2
            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        
        return left