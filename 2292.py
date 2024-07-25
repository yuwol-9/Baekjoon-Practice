
N = int(input())

Box = 1
T = 1

while N > Box:
    Box += 6 * T
    T += 1
print(T)