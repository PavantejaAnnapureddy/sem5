# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    running_sum = 0
    already_good = True
    for x in a:
        running_sum += x
        if running_sum < 0:
            already_good = False
            break
    
    if already_good:
        print("YES")
        continue
    found = False
    for skip in range(n):
        running_sum = 0
        good = True
        for i in range(n):
            if i == skip:
                continue
            running_sum += a[i]
            if running_sum < 0:
                good = False
                break
        if good:
            found = True
            break
    
    print("YES" if found else "NO")