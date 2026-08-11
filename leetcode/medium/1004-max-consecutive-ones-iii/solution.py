class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0  
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
#from collections import Counter
"""
#class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        window_count = Counter()  
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            window_count[nums[right]] += 1
            
            while window_count[0] > k:
                window_count[nums[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len"""