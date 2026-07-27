# 3Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

 **Example 1:** 

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

```

 **Example 2:** 

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

```

 **Example 3:** 

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

```

 

 **Constraints:** 

- 3 <= nums.length <= 3000
- -105 <= nums[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 544 ms (beats 80.55%)  
**Memory:** 22.3 MB (beats 53.49%)  
**Submitted:** 2026-07-27T09:05:05.073Z  

```py
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Sort the array
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        result = []
        n = len(nums)
        
        # Step 2: Fix the first element
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Set up two pointers
            left = i + 1
            right = n - 1
            target = -nums[i]  # What we need left+right to equal
            
            # Step 4: Move pointers towards each other
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < target:
                    # Sum is too small, move left right (increase sum)
                    left += 1
                else:
                    # Sum is too large, move right left (decrease sum)
                    right -= 1
        
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/3sum/)