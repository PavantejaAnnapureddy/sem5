import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        
        pos = [0] * (N + 1)
        for i, val in enumerate(P, 1):
            pos[val] = i
        
        K = (N + 1) // 2
        L = [0] * (K + 1)
        R = [0] * (K + 1)
        
        min_pos = N + 1
        max_pos = 0
        possible = True
        
        for i in range(1, K + 1):
            min_pos = min(min_pos, pos[i])
            max_pos = max(max_pos, pos[i])
            
            if max_pos - min_pos + 1 > 2 * i - 1:
                possible = False
                break
            
            if i == 1:
                L[i] = R[i] = pos[1]
            else:
                cur_L = min(min_pos, L[i-1])
                cur_R = max(max_pos, R[i-1])
                target_len = 2 * i - 1
                while cur_R - cur_L + 1 < target_len:
                    if cur_L > 1:
                        cur_L -= 1
                    elif cur_R < N:
                        cur_R += 1
                    else:
                        possible = False
                        break
                
                if not possible:
                    break
                
                L[i] = cur_L
                R[i] = cur_R
        
        if not possible:
            print(-1)
        else:
            for i in range(1, K + 1):
                print(L[i], R[i])

if __name__ == "__main__":
    solve()