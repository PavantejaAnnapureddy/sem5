class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(divisor: int) -> bool:
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
                if total > threshold:
                    return False
            return True
        
        left = 1
        right = max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        