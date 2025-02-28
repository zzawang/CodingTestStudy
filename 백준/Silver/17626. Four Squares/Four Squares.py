import sys

n = int(sys.stdin.readline())
dp = [float("inf")] * 50001
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    if i == int(i ** 0.5) ** 2:
        dp[i] = 1
        continue
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])

print(dp[n])