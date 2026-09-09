
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    days = 1
    while True:
        sum_squares = days * (days + 1) * (2 * days + 1) // 6
        profit = Y * sum_squares - days * X
        
        if profit > 0:
            print(days)
            break
        days += 1