import sys

Rick = ['Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye','Never gonna tell a lie and hurt you','Never gonna stop']
N = int(input())
L = list(sys.stdin.readline().strip('\n') for _ in range(N))

Cnt = True
for i in L:
    if i not in Rick:
        print('Yes')
        Cnt = False
        break
if Cnt:
    print('No')
        