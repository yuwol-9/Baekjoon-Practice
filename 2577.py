A = int(input())
B = int(input())
C = int(input())

Num = list(map(int, str(A * B * C)))

for i in range(0,10):
    print(Num.count(i))