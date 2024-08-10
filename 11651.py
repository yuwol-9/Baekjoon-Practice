import sys

N = int(input())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

SL = sorted(L, key = lambda x:(x[1],x[0]))

for i in SL:
    print(i[0],i[1])
