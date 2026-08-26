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
    
    flag2 = False
    for i in range(1, n - 1):
        if s[i - 1] == s[i + 1] and s[i - 1] != s[i]:
            flag2 = True
            break
    
    if flag2:
        print(min(n - 1, initial + 2))
        continue
    
    is_0_1 = True
    seen_1 = False
    for c in s:
        if c == '1':
            seen_1 = True
        if seen_1 and c == '0':
            is_0_1 = False
            break
    
    is_1_0 = True
    seen_0 = False
    for c in s:
        if c == '0':
            seen_0 = True
        if seen_0 and c == '1':
            is_1_0 = False
            break
    
    if not (is_0_1 or is_1_0):
        print(min(n - 1, initial + 1))
    else:
        print(initial)