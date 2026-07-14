# Max Consecutive Ones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a binary array `nums`, return  *the maximum number of consecutive* `1` *'s in the array*.

 

 **Example 1:** 

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

```

 **Example 2:** 

```
Input: nums = [1,0,1,1,0,1]
Output: 2

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- nums[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 85.09%)  
**Memory:** 22 MB (beats 5.15%)  
**Submitted:** 2026-07-14T10:19:57.838Z  

```py
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:  
                max_count = max(max_count, count)  
                count = 0  
        max_count = max(max_count, count)
        
        return max_count
```

---

[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)