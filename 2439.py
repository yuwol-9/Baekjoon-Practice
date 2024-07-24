n = int(input())
k = 1
while n != 0:
    for _ in range(0,n-1):
        print(" ", end = "")
    for _ in range(0,k):
        print("*", end = "")
    print()
    n -= 1
    k += 1