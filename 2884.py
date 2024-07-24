Num = list(map(int, input().split()))

if Num[1] < 45:
    if Num[0] == 0:
        Num[0] = 24
    print(Num[0] - 1, 60 - (45 - Num[1]))
else:
    print(Num[0], Num[1] - 45)