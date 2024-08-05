import sys
input = sys.stdin.readline

N, K = map(int, input().split())

R = 1
for i in range(K):
    R *= N
    N -= 1

D = 1
for i in range(2, K+1):
    D *= i
    
print(R // D)