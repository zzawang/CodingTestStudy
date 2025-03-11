import sys

# 선영이가 지금까지 i개의 숫자를 골랐을 때, 숫자 j를 고르는 경우의 수
dp = [[0] * 2001 for _ in range(11)]
answer = 0

dp[0][0] = 1
for i in range(1, 11):
    for j in range(1, 2001):
        dp[i][j] = sum(dp[i - 1][k] for k in range(j // 2 + 1))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    # 선택하는 로또 개수 n, 로또 숫자 m
    n, m = map(int, sys.stdin.readline().rstrip().split())
    print(sum(dp[n][:m + 1]))