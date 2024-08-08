
N = int(input())
L = []

for _ in range(N):
    x, y = list(input().split())
    L.append([int(x),y])

L = sorted(L, key=lambda x: x[0])

for i in range(N):
    for j in L[i]:
        print(j, end=' ')
    print()