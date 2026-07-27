class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Sort the array
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        result = []
        n = len(nums)
        
        # Step 2: Fix the first element
        for i in range(n - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Set up two pointers
            left = i + 1
            right = n - 1
            target = -nums[i]  # What we need left+right to equal
            
            # Step 4: Move pointers towards each other
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < target:
                    # Sum is too small, move left right (increase sum)
                    left += 1
                else:
                    # Sum is too large, move right left (decrease sum)
                    right -= 1
        
        return result