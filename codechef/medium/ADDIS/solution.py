# cook your dish here
import math

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    from collections import Counter
    freq = Counter(A)
    max_freq = max(freq.values())
    
    print((max_freq + 1) // 2)  