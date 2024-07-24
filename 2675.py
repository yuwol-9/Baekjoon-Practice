T = int(input())
while T != 0:
    N, Word = list(map(str, input().split()))
    Num = int(N)
    L = []

    for x in Word:
        L.append(x * Num)

    print("".join(L))
    T -= 1