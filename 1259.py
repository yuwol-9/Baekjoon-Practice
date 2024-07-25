
while True:
    N = input()
    if N == '0':
        break
    NR = N[::-1]
    if N == NR:
        print("yes")
    else:
        print("no")