
import sys

N = int(input())
L = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

L.sort()

for i in L:
    print(i[0],i[1])