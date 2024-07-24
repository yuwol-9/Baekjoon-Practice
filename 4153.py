
while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    else:
        Num = sorted([A, B, C])
        A, B, C = Num[0], Num[1], Num[2]
        if A * A + B * B == C * C:
            print("right")
        else:
            print("wrong")