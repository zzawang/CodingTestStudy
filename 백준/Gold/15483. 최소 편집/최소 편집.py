words1 = input()
words2 = input()
length1 = len(words1)
length2 = len(words2)

dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    dp[i][0] = i

for j in range(1, length2 + 1):
    dp[0][j] = j

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if words1[i - 1] == words2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1


print(dp[length1][length2])