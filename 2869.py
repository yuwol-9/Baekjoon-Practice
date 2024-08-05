A, B, V = map(int, input().split())

M = (V - A) // (A - B)
N = (V - A) % (A - B)

if N == 0:
    print(M + 1)
else:
    print(M + 2)