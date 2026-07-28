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