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