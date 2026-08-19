# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    odd_count = sum(1 for x in arr if x % 2 == 1)
    even_count = N - odd_count
    
    if odd_count == even_count:
        print(2 * odd_count)
    else:
        print(2 * min(odd_count, even_count) + 1)