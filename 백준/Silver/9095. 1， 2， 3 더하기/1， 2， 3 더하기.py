import sys

dp = [1] * 11
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])