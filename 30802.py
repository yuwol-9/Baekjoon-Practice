
N = int(input())
Size = list(map(int, input().split()))
T, P = map(int, input().split())

TshirtNum = 0
for i in Size:
    if i % T != 0:
        TshirtNum += (i // T) + 1
    else:
        TshirtNum += i // T
 
Pens = N // P
Pen = N % P

print(TshirtNum)
print(Pens, Pen)