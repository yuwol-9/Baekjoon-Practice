import itertools

N, M = map(int, input().split())
Card = list(map(int, input().split()))

Ccomb = list(itertools.combinations(Card, 3))
Box = 0

for i in Ccomb:
    if sum(i) <= M:
        Box = max(Box, sum(i))

print(Box)