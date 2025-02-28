import sys

n = int(sys.stdin.readline())
permutations = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * 1001
dp[1] = permutations[1]

for i in range(2, n + 1):
    dp[i] = permutations[i]
    for j in range(1, i):
        if permutations[i] > permutations[j]:
            dp[i] = max(dp[i], dp[j] + permutations[i])

print(max(dp))
