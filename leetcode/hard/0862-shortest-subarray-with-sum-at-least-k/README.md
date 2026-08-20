# Shortest Subarray with Sum at Least K

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an integer array `nums` and an integer `k`, return  *the length of the shortest non-empty  **subarray**  of* `nums` *with a sum of at least* `k`. If there is no such  **subarray**, return `-1`.

A  **subarray**  is a  **contiguous**  part of an array.

 

 **Example 1:** 

```
Input: nums = [1], k = 1
Output: 1

```

 **Example 2:** 

```
Input: nums = [1,2], k = 4
Output: -1

```

 **Example 3:** 

```
Input: nums = [2,-1,2], k = 3
Output: 3

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -105 <= nums[i] <= 105
- 1 <= k <= 109

## Solution

**Language:** Python  
**Runtime:** 225 ms (beats 11.45%)  
**Memory:** 29.8 MB (beats 21.48%)  
**Submitted:** 2026-08-20T15:36:04.722Z  

```py
from typing import List
import heapq

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = float('inf')
        heap = []

        for i in range(n + 1):
            while heap and pref[i] - heap[0][0] >= k:
                val, idx = heapq.heappop(heap)
                ans = min(ans, i - idx)
            heapq.heappush(heap, (pref[i], i))

        return -1 if ans == float('inf') else ans
```

---

[View on LeetCode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)