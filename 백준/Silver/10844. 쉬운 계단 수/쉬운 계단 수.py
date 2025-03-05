import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(101)] # 길이가 i이면서 이전 자리의 수가 j인 계단수의 개수
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]  # 0은 이전 자리 숫자가 1인 경우만 가능
        elif j == 9:
            dp[i][j] = dp[i - 1][8]  # 9는 이전 자리 숫자가 8인 경우만 가능
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000

# 길이가 n인 계단 수의 총 개수
print(sum(dp[n]) % 1000000000)