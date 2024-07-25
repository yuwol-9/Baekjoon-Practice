
N = int(input())
Score = list(map(float, input().split()))
NewScore = 0;

for i in Score:
    Box = (i / max(Score)) * 100
    NewScore += Box

print(NewScore / N)