"""T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    total = sum(A)
    alice = 0
    
    while total > 0:
        if total % 2 == 0:
            ate = False
            for i in range(N):
                if A[i] >= 2:
                    A[i] -= 2
                    alice += 2
                    total -= 2
                    ate = True
                    break
            if not ate:
                for i in range(N):
                    if A[i] == 1:
                        A[i] = 0
                        alice += 1
                        total -= 1
                        break
        else:
            ate = False
            for i in range(N):
                if A[i] >= 2:
                    A[i] -= 2
                    total -= 2
                    ate = True
                    break
            if not ate:
           
                for i in range(N):
                    if A[i] == 1:
                        A[i] = 0
                        total -= 1
                        break
    
    print(alice)"""
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    total = sum(A)
    alice = 0
    
    while total > 0:
        if total % 2 == 0:
            max_idx = max(range(N), key=lambda i: A[i])
            
            if A[max_idx] >= 2:
                A[max_idx] -= 2
                alice += 2
                total -= 2
            else:
                A[max_idx] -= 1
                alice += 1
                total -= 1
        else:
            max_idx = max(range(N), key=lambda i: A[i])
            
            if A[max_idx] >= 2:
                A[max_idx] -= 2
                total -= 2
            else:
                A[max_idx] -= 1
                total -= 1
    
    print(alice)