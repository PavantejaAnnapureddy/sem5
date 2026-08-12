# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    ans = float('inf')
    curr = N 
    ops = 0
    while curr%3 !=0:
        curr +=1
        ops +=1
    ans = min(ans, ops)
    curr = N 
    ops=0
    if curr %5 !=0:
        ops +=1
        curr =((curr // 5)+1)*5
    else:
        ops +=1
        curr+= 5
    while curr %3 !=0:
        curr +=1
        ops+=1
    ans = min(ans, ops)
    print(ans)
"""T = int(input())

for _ in range(T):
    N = int(input())
    
    # Strategy 1: Only add 1s
    if N % 3 == 0:
        ans = 0
    elif N % 3 == 1:
        ans = 2
    else:  # N % 3 == 2
        ans = 1
    
   
    next_multiple_of_5 = ((N // 5) + 1) * 5
    
    ops = 1  # for the jump
    if next_multiple_of_5 % 3 == 0:
        ops += 0
    elif next_multiple_of_5 % 3 == 1:
        ops += 2
    else:  # next_multiple_of_5 % 3 == 2
        ops += 1
    
    ans = min(ans, ops)
    print(ans)