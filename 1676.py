import math

N = int(input())
F  = list(map(int, str(math.factorial(N))))
F.reverse()
Z = 0

for i in range(len(F)):
    if F[i] != 0:
        break
    Z += 1
print(Z)