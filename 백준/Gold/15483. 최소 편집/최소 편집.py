words1 = [0] + list(input())
words2 = [0] + list(input())

dp1 = [0] + [i for i in range(1, len(words1))]
dp2 = [0] + [i for i in range(1, len(words2))]

dp = [[0] * len(words2) for _ in range(len(words1))]

for i in range(len(words1)):
    for j in range(len(words2)):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i


for i in range(1, len(words1)):
    for j in range(1, len(words2)):
        if words1[i] == words2[j]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

print(dp[len(words1) - 1][len(words2) - 1])