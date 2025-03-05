import sys

N, M = map(int, sys.stdin.readline().rstrip().split())  # 표의 크기 N과 합을 구해야 하는 횟수 M

table = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    table[i] = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]  # (0, 0) ~ (i, j) 까지의 합
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = table[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    answer = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(answer)
