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
    
    for i in range(n - 1):
        if s[i] != s[i+1]:
            new_s = s[:i] + s[i+1] + s[i] + s[i+2:]
            new_beauty = 0
            for j in range(n - 1):
                if new_s[j] == new_s[j+1]:
                    new_beauty += 1
            ans = max(ans, new_beauty)
    
    for i in range(n - 2):
        new_s = s[:i] + s[i+2] + s[i+1] + s[i] + s[i+3:]
        new_beauty = 0
        for j in range(n - 1):
            if new_s[j] == new_s[j+1]:
                new_beauty += 1
        ans = max(ans, new_beauty)
    
    print(min(ans, n - 1))