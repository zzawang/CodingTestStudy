import sys

n = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0] * n
prefix_sum[0] = x[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + x[i]

answer = 0
for i in range(n):
    answer += (x[i] * (prefix_sum[n - 1] - prefix_sum[i]))
print(answer)