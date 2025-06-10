n = int(input())
INF = 50
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = dist[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_score = INF
candidates = []

for i in range(1, n + 1):
    score = max(dist[i][1:])
    if score < min_score:
        min_score = score
        candidates = [i]
    elif score == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)
