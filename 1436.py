N = int(input())
Ans = 666
Cnt = 0

while Cnt < N:
    if '666' in str(Ans):
        Cnt += 1
        if Cnt == N:
            break
    Ans += 1
print(Ans)