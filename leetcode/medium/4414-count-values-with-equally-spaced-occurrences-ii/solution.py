class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        from  collections import defaultdict
        velquorani = nums
        positions = defaultdict(list)
        for i, num in enumerate(velquorani):
            positions[num].append(i)
        count = 0
        for indices in positions.values():
            if len(indices) < 3:
                continue
            diffs ={indices[j+1] - indices[j] for j in   range(len(indices)-1)}
            if len(diffs) == 1:
                count +=1
        return count
            