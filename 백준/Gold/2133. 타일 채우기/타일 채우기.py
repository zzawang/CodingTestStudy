import sys

N = int(sys.stdin.readline().rstrip())
dp = [0] * 31
dp[2] = 3

for i in range(4, 31):
    if i % 2 == 0:
        dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2

print(dp[N])