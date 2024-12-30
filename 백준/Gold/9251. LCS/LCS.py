list1 = [word for word in input()]
list2 = [word for word in input()]

dp = [[0] * (len(list2) + 1) for _ in range(len(list1) + 1)]

for i1 in range(1, len(list1) + 1):
    for i2 in range(1, len(list2) + 1):
        if list1[i1 - 1] == list2[i2 - 1]:
            dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
        else:
            dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

print(dp[len(list1)][len(list2)])
