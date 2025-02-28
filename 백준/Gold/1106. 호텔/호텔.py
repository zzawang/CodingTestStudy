import sys

c, n = map(int, sys.stdin.readline().rstrip().split())
data = []
dp = [float("inf")] * (c + 100)
dp[0] = 0

for _ in range(n):
    _v, _p = map(int, sys.stdin.readline().rstrip().split())
    data.append((_v, _p))

for v, p in data:
    for i in range(1, c + 100):
        if i >= p:
            dp[i] = min(dp[i], dp[i - p] + v)

print(min(dp[c:]))