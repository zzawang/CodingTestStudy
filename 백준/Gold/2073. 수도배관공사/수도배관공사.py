import sys

D, P = map(int, sys.stdin.readline().rstrip().split())

length = []
capabilities = []
for _ in range(P):
    L, C = map(int, sys.stdin.readline().rstrip().split())
    length.append(L)
    capabilities.append(C)

dp = [[0] * (P + 1) for _ in range(D + 1)]
for i in range(1, D + 1):
    for j in range(1, P + 1):
        l, c = length[j - 1], capabilities[j - 1]
        if i < l:
            dp[i][j] = dp[i][j - 1]
        elif i == l:
            dp[i][j] = max(dp[i][j - 1], c)
        else:
            dp[i][j] = max(dp[i][j - 1], min(dp[i - l][j - 1], c))

print(dp[D][P])