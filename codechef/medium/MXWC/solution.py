# cook your dish here
n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1
max_water = 0

while left < right:
    width = right - left
    min_height = min(height[left], height[right])
    water = width * min_height
    
    # Update maximum water
    max_water = max(max_water, water)
    
    # Move the pointer pointing to the shorter line
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_water)