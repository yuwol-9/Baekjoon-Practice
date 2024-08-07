import sys

N = int(input())
NumL = [int(sys.stdin.readline().strip()) for i in range(N)]
NumL.sort()

for i in NumL:
    print(i)