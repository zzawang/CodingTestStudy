import sys

N = int(sys.stdin.readline().rstrip())  # 돌의 개수
A = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [float("inf")] * N
dp[0] = 0

for j in range(N):
    for i in range(j):
        power = max(dp[i], (j - i) * (1 + abs(A[i] - A[j])))
        dp[j] = min(dp[j], power)

print(dp[-1])
