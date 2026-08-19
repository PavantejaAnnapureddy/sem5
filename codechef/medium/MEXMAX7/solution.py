# cook your dish here
MOD = 998244353

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    freq = [0] * (N + 2)
    for x in A:
        freq[x] += 1
    
    ans = 0
    
    for m in range(N + 1):
        if freq[m] == 0:
            continue
        max_val = m - 1
        if max_val < 0:
            continue
        if max_val >= 0 and freq[max_val] == 0:
            continue
        
        possible = True
        for i in range(m - 1):
            if freq[i] == 0:
                possible = False
                break
        if not possible:
            continue
        
        ways = 1
        for i in range(m - 1):
            ways = (ways * pow(2, freq[i], MOD)) % MOD
        
        ways = (ways * (pow(2, freq[m-1], MOD) - 1)) % MOD
        
        ans = (ans + ways) % MOD
    
    for m in range(N):
        max_val = m + 1
        if freq[m] == 0 or freq[m+1] == 0:
            continue
        
        possible = True
        for i in range(m):
            if freq[i] == 0:
                possible = False
                break
        if not possible:
            continue
        
        if freq[m] > 0:
            continue
        
        ways = 1
        for i in range(m):
            ways = (ways * pow(2, freq[i], MOD)) % MOD
        
        ways = (ways * (pow(2, freq[m+1], MOD) - 1)) % MOD
        
        ans = (ans + ways) % MOD
    
    print(ans)