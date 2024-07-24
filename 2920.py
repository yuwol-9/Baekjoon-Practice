Music = list(map(int, input().split()))
As = [1, 2, 3, 4, 5, 6, 7, 8]
De = [8, 7, 6, 5, 4, 3, 2, 1]

if Music == As:
    print("ascending")
elif Music == De:
    print("descending")
else:
    print("mixed")