import math

T = int(input())
Num = map(int, input().split())
Total = 0;

for i in Num:
    if i < 2:
        continue
    IsPrime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            IsPrime = False
            break
    if IsPrime:
        Total += 1

print(Total)