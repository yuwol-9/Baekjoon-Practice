
nums = input().split()
total = 0
for x in nums:
    total = total + int(x)*int(x)
print(total % 10)