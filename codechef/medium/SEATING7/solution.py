# cook your dish here
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    occupied_seats = list(map(int, input().split()))
    
    occupied = [False] * (n + 1)
    for seat in occupied_seats:
        occupied[seat] = True
    
    result = []
    ptr = 1  
    for _ in range(k):
        while occupied[ptr]:
            ptr += 1
        occupied[ptr] = True
        result.append(ptr)
    
    print(' '.join(map(str, result)))