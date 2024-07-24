T = int(input())

while T != 0:
    H, W, N = map(int, input().split())

    F = str((N // H) + 1)
    L = str(N % H)

    if len(F) < 2:
        print(L  + str(0) + F)
    else:
        print(L + F)
    T -= 1