T = int(input())

while T > 0:
    k = int(input())
    n = int(input())
    Floor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    for _ in range(1,k+1):
        for i in range(1,n):
            Floor[i] = Floor[i-1] + Floor[i]
    print(Floor[n-1])
    T -= 1