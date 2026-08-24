# Subarray Sum Equals K

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` and an integer `k`, return  *the total number of subarrays whose sum equals to*  `k`.

A subarray is a contiguous  **non-empty**  sequence of elements within an array.

 

 **Example 1:** 

```
Input: nums = [1,1,1], k = 2
Output: 2

```

 **Example 2:** 

```
Input: nums = [1,2,3], k = 3
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -1000 <= nums[i] <= 1000
- -107 <= k <= 107

## Solution

**Language:** Python  
**Runtime:** 38 ms (beats 29.66%)  
**Memory:** 21.8 MB (beats 56.38%)  
**Submitted:** 2026-08-24T09:24:26.090Z  

```py
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefsum = 0
        pref = {0: 1}
        
        for num in nums:
            prefsum += num
            
            if (prefsum - k) in pref:
                count += pref[prefsum - k]
            
            pref[prefsum] = pref.get(prefsum, 0) + 1
        
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)