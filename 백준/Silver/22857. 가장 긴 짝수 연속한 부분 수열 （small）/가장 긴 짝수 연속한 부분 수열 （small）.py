n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    s[i] %= 2  # 짝수(0), 홀수(1)로 변환
    for j in range(k+1):
        if s[i] == 0:  # 현재 숫자가 짝수일 때
            dp[i][j] = dp[i-1][j] + 1  # 이전 값에서 이어서 증가
        elif j != 0 and s[i]:  # 현재 숫자가 홀수이고, j가 0이 아닐 때 (즉, 삭제 가능)
            dp[i][j] = dp[i-1][j-1]  # 홀수를 삭제했으므로 길이는 증가하지 않음

result = []
for i in dp:
    result.append(i[k])

print(max(result))