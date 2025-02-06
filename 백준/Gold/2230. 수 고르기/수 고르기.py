import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

answer = float('inf')
start, end = 0, 0

while start <= end < n:
    result = nums[end] - nums[start]

    if result == m:
        print(m)
        exit()
    elif result > m:
        answer = min(answer, result)
        start += 1
    else:
        end += 1

print(answer)