class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # ← ADD THIS
        result = set()
        n = len(nums)
        
        for i in range(n - 2):  # ← CHANGE to n-2
            if i > 0 and nums[i] == nums[i-1]:  # ← ADD THIS
                continue
            seen = set()
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    # tuple(sorted(...)) is now safe because of sorting
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)
                seen.add(nums[j])
        
        return [list(t) for t in result]