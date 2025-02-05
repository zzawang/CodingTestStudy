N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

answer = 0
for c in coins:
    if K // c == 0:
        continue
    div, mod = divmod(K, c)
    K = mod
    answer += div

print(answer)