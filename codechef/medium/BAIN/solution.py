
from itertools import combinations

a, b, c, d = map(int, input().split())
arr = [a, b, c, d]

for r in range(1, 5):  
    for combo in combinations(arr, r):
        if sum(combo) == 0:
            print("Yes")
            exit()

print("No")