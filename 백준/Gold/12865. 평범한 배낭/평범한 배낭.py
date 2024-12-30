n, k = map(int, input().split())
knapsacks = []
for _ in range(n):
    w, v = map(int, input().split())
    knapsacks.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):  # 각 물건의 무게와 가치
    weight, value = knapsacks[i - 1]
    for j in range(1, k + 1):  # 최대 j를 담을 수 있는 배낭
        if weight > j:  # 가방의 최대 무게를 초과하는 물건은 가방에 넣을 수 없으므로
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])