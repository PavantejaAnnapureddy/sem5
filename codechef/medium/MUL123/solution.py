# cook your dish here
T=int(input())
for_ in range(T):
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