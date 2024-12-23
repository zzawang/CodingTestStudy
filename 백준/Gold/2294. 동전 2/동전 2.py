n, k = map(int, input().split())
coins = set() #  가치가 같은 동전이 여러 번 주어질 수도 있으므로 set으로 선언
dp = [100001 for _ in range(k + 1)]
dp[0] = 0

for num in range(n):
    coins.add(int(input()))

for coin in coins:
    for i in range(coin, k + 1): # coin 미만의 값은 변하지 않으므로
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != 100001 else -1)