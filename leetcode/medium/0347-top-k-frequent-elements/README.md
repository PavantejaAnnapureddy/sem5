# Top K Frequent Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` and an integer `k`, return  *the*  `k`  *most frequent elements*. You may return the answer in  **any order**.

 

 **Example 1:** 

 **Input:**  nums = [1,1,1,2,2,3], k = 2

 **Output:**  [1,2]

 **Example 2:** 

 **Input:**  nums = [1], k = 1

 **Output:**  [1]

 **Example 3:** 

 **Input:**  nums = [1,2,1,2,1,2,3,1,3,2], k = 2

 **Output:**  [1,2]

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

 

 **Follow up:**  Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 51.85%)  
**Memory:** 24.8 MB (beats 12.48%)  
**Submitted:** 2026-08-10T09:00:09.872Z  

```py
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)