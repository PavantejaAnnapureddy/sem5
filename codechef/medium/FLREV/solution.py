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
    
    ans = initial
    
    for i in range(1, n - 1):
        if s[i-1] == s[i+1] and s[i-1] != s[i]:
            ans = max(ans, initial + 2)
    
    has_same_after_diff = False
    for i in range(n - 2):
        if s[i] != s[i+1] and s[i] == s[i+2]:
            has_same_after_diff = True
            break
    
    if has_same_after_diff:
        ans = max(ans, initial + 1)
    
    print(min(ans, n - 1))