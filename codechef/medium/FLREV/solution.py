t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # initial beauty
    b = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            b += 1

    # if already maximum
    if b == n - 1:
        print(b)
        continue

    # check if +2 is possible
    first_01 = -1
    first_10 = -1
    plus2 = False

    for i in range(n - 1):
        if s[i] != s[i + 1]:
            if s[i] == '0':  # pattern "01"
                if first_01 != -1 and first_01 + 2 <= i:
                    plus2 = True
                    break
                if first_01 == -1:
                    first_01 = i
            else:  # pattern "10"
                if first_10 != -1 and first_10 + 2 <= i:
                    plus2 = True
                    break
                if first_10 == -1:
                    first_10 = i

    if plus2:
        print(min(n - 1, b + 2))
        continue

    # count number of different adjacent pairs
    diff = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            diff += 1

    if diff >= 2:
        print(min(n - 1, b + 1))
    else:
        print(b)