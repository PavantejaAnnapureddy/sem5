# Sliding Window Maximum

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return  *the max sliding window*.

 

 **Example 1:** 

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```

 **Example 2:** 

```
Input: nums = [1], k = 1
Output: [1]

```

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- 1 <= k <= nums.length

## Solution

**Language:** Python  
**Runtime:** 203 ms (beats 32.37%)  
**Memory:** 35.5 MB (beats 26.10%)  
**Submitted:** 2026-09-28T09:03:04.173Z  

```py
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()          # stores indices
        result = []

        for i, num in enumerate(nums):
            # Remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values from back (they'll never be max)
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Window has reached size k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
```

---

[View on LeetCode](https://leetcode.com/problems/sliding-window-maximum/)