Num = []

for _ in range(1,10):
    n = int(input())
    Num.append(n)

M = max(Num)
print(M)
print(Num.index(M) + 1)