
Num = int(input())


for i in range(1,Num+1):
    NumSum = i + sum(map(int, str(i)))
    if NumSum == Num:
        print(i)
        break
    elif i == Num:
        print(0)