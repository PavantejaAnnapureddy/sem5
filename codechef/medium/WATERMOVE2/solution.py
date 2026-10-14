# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k >= n - 1:
        print(sum(a))
    else:
        a.sort(reverse=True)
        print(sum(a[:k+1]))