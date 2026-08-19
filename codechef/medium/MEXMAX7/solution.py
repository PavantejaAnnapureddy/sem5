# cook your dish here
MOD = 998244353

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    freq = [0] * (N + 2)
    for x in A:
        freq[x] += 1
    
    pow2 = [1] * (N + 2)
    for i in range(1, N + 2):
        pow2[i] = (pow2[i - 1] * 2) % MOD
    
    ways = [0] * (N + 2)
    for i in range(N + 2):
        ways[i] = (pow2[freq[i]] - 1) % MOD
    
    pref = [1] * (N + 2)
    pref[0] = ways[0]
    for i in range(1, N + 2):
        pref[i] = (pref[i - 1] * ways[i]) % MOD
    
    ans = 0
    
    for m in range(1, N + 1):
        prod = pref[m - 1]
        ans = (ans + prod) % MOD
    
    for m in range(0, N):
        prod = pref[m - 1] if m > 0 else 1
        prod = (prod * ways[m + 1]) % MOD
        ans = (ans + prod) % MOD
    
    print(ans)