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
**Runtime:** 911 ms (beats 18.08%)  
**Memory:** 24.1 MB (beats 5.05%)  
**Submitted:** 2026-07-27T09:03:15.747Z  

```py
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # ← ADD THIS
        result = set()
        n = len(nums)
        
        for i in range(n - 2):  # ← CHANGE to n-2
            if i > 0 and nums[i] == nums[i-1]:  # ← ADD THIS
                continue
            seen = set()
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    # tuple(sorted(...)) is now safe because of sorting
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)
                seen.add(nums[j])
        
        return [list(t) for t in result]
```

---

[View on LeetCode](https://leetcode.com/problems/3sum/)