# Shortest Unsorted Continuous Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, you need to find one  **continuous subarray**  such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return  *the shortest such subarray and output its length*.

 

 **Example 1:** 

```
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

```

 **Example 2:** 

```
Input: nums = [1,2,3,4]
Output: 0

```

 **Example 3:** 

```
Input: nums = [1]
Output: 0

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -105 <= nums[i] <= 105

 

 **Follow up:**  Can you solve it in `O(n)` time complexity?

## Solution

**Language:** Python  
**Runtime:** 6 ms (beats 85.41%)  
**Memory:** 20.5 MB (beats 82.95%)  
**Submitted:** 2026-08-11T08:55:23.068Z  

```py
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = -1, -2 
        
        max_seen = float('-inf')
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]
        
        min_seen = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]
        
        return right - left + 1
```

---

[View on LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)