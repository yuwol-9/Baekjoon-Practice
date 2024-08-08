
N = int(input())
L = []
Ans = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append((x,y))

for i in range(N):
    Cnt = 0
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            Cnt += 1
    Ans.append(Cnt+1)
    
for K in Ans:
    print(K, end=" ")