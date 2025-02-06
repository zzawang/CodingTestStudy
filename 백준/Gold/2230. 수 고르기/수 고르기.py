import sys

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
answer = sys.maxsize
start, end = 0, 0

while start <= end < n:
    result = nums[end] - nums[start]

    if result >= m:
        answer = min(answer, result)
        start += 1
    else:
        end += 1

print(answer)