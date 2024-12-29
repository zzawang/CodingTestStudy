n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * 10001
dp[0] = 1

for coin in coins:
    for num in range(coin, k + 1):
        dp[num] += dp[num - coin]

print(dp[k])