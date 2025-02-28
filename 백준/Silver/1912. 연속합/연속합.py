import sys

n = int(sys.stdin.readline().rstrip())
permutations = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = permutations[1]
max_num = dp[1]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + permutations[i], permutations[i])
    max_num = max(max_num, dp[i])

print(max_num)
