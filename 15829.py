
L = int(input())
S = input().strip()

r = 31
M = 1234567891
HashValue = 0

for i in range(L):
    C = ord(S[i]) - ord('a') + 1
    HashValue = (HashValue + C * (r ** i)) % M

print(HashValue)