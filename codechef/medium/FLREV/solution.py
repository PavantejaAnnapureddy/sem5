t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    initial = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            initial += 1
    
    if initial == n - 1:
        print(initial)
        continue
    
    max_beauty = initial
    
    for i in range(1, n - 1):
        if s[i-1] == s[i+1] and s[i-1] != s[i]:
            max_beauty = max(max_beauty, initial + 2)
    
    if initial + 1 <= n - 1:
        max_beauty = max(max_beauty, initial + 1)
    
    print(min(max_beauty, n - 1))