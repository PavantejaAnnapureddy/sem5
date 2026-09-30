# cook your dish here
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = Counter()
    for i in range(n):
        v = a[i] - i  # using 0-indexed i, equivalent to a[i] - (i+1) + 1 = a[i] - i
        freq[v] += 1
    
    max_match = max(freq.values())
    print(n - max_match)