N = int(input())
L = [[] for i in range(51)]

for _ in range(N):
    W = input()
    if W not in L[len(W)]:
        L[len(W)].append(W)
        L[len(W)].sort()

for i in L:
    if i != []:
        for j in i:
            print(j)