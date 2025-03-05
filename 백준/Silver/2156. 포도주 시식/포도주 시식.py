import sys
n = int(sys.stdin.readline())
drink = [0] * 10001
for i in range(n):
    drink[i] = int(sys.stdin.readline())

dp = [0] * 10001
dp[0] = drink[0]
dp[1] = dp[0] + drink[1]
dp[2] = max(drink[0] + drink[2], drink[1] + drink[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + drink[i - 1] + drink[i], dp[i - 2] + drink[i], dp[i - 1])

print(max(dp))