import sys

n = int(sys.stdin.readline().rstrip())
time = [0]
price = [0]

for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    time.append(t)
    price.append(p)

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1]) # 이전까지의 최댓값
    final_date = i + time[i] - 1 # 당일 포함!!
    if final_date <= n: # 최종일 안에 일이 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        dp[final_date] = max(dp[final_date], dp[i - 1] + price[i])

print(max(dp))