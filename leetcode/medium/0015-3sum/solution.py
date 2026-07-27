class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i] + nums[j])
                k = bisect.bisect_left(nums, target, j + 1, n)
                if k < n and nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
        
        return result