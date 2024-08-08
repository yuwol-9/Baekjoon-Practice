import sys

NumL = list(int(sys.stdin.readline().strip()) for _ in range(10))
M = 0
for i in NumL:
    Cnt = NumL.count(i)
    if Cnt > NumL.count(M):
        M = i
        

print(sum(NumL)//10)
print(M)