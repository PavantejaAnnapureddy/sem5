# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `arr` and two integers `k` and `threshold`, return  *the number of sub-arrays of size* `k` *and average greater than or equal to* `threshold`.

 

 **Example 1:** 

```
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

```

 **Example 2:** 

```
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

```

 

 **Constraints:** 

- 1 <= arr.length <= 105
- 1 <= arr[i] <= 104
- 1 <= k <= arr.length
- 0 <= threshold <= 104

## Solution

**Language:** Python  
**Runtime:** 37 ms (beats 80.61%)  
**Memory:** 30.2 MB (beats 28.33%)  
**Submitted:** 2026-07-28T10:40:37.206Z  

```py
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Calculate sum of first window
        window_sum = sum(arr[:k])
        count = 0
        
        # Check first window
        if window_sum / k >= threshold:
            count += 1
        
        # Slide the window
        for i in range(k, len(arr)):
            # Update window sum
            window_sum = window_sum - arr[i - k] + arr[i]
            
            # Check if average >= threshold
            if window_sum / k >= threshold:
                count += 1
        
        return count
```

---

[View on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)