# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 2:
        print(0)
    else:
        a.sort()
        option1 = a[-1] - a[1]
        option2 = a[-2] - a[0]
        print(min(option1, option2))