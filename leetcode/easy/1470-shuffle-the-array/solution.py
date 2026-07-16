class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]          # Even indices get x values
            result[2 * i + 1] = nums[i + n]  # Odd indices get y values
        return result