import sys

D, P = map(int, sys.stdin.readline().rstrip().split())

dp = [1e9] + [0] * D
for _ in range(P):
    L, C = map(int, sys.stdin.readline().rstrip().split())
    tmp = dp[:]
    for i in range(L, D + 1):
        if tmp[i - L]: # 최대 비용이 저장되어 있는 경우만 진행
            dp[i] = max(dp[i], min(tmp[i - L], C))

print(dp[D])