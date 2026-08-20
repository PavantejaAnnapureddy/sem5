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