
N, M = map(int, input().split())

GN = N
GM = M

while GM > 0:
    GN, GM = GM, GN % GM
Gcd = GN

Lcm = N * M // Gcd
        
print(Gcd)
print(Lcm)