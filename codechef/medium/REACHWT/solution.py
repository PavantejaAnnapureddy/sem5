# cook your dish here
y = int(input())
for _ in range(y):
    x=int(input())
    if x % 2 == 0:
        cost = (x // 2) * 30
    else:
        cost = (x // 2) * 30 + 20
    print(cost)
    
    