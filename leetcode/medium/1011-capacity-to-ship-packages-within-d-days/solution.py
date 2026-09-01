class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            days_needed = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    days_needed += 1
                    current = w
                    if days_needed > days:
                        return False
                else:
                    current += w
            return True
        
        left = max(weights)  
        right = sum(weights) 
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left