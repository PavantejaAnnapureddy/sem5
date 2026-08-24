class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        total_sum = prefix[n]  # sum of all elements
        
        for i in range(n):
            if prefix[i] == total_sum - prefix[i] - nums[i]:
                return i
        
        return -1