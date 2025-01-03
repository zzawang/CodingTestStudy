n = int(input())
nums = list(map(int, input().split()))

d1 = [1] * n
d2 = [1] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and d1[i] <= d1[j]:
            d1[i] = d1[j]+1

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if nums[i] > nums[j] and d2[i] <= d2[j]:
            d2[i] = d2[j] + 1

for i in range(n):
    d1[i] = d1[i] + d2[i] - 1

print(max(d1))
