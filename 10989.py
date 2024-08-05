import sys
input = sys.stdin.readline

N = int(input())
Cnt = [0] * (10000 + 1)

for _ in range(N):
    Cnt[int(input())] += 1

for i in range(len(Cnt)):
    for _ in range(Cnt[i]):
        print(i, end = "\n")