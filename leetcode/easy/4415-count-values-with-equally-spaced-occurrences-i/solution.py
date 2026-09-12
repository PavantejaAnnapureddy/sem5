class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        from collections import defaultdict
        positions = defaultdict(list)
        for i, num in enumerate(nums):
           positions[num].append(i)
        count =0
        for num, indices in positions.items():
            if len(indices) == 3:
                if indices[1] - indices[0] == indices[2] - indices[1]:
                    count += 1
        return count
        