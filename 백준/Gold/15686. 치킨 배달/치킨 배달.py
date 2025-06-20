from itertools import combinations

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i + 1, j + 1))
        elif graph[i][j] == 2:
            chicken.append((i + 1, j + 1))

answer = n * 2 * len(house)
combinations = list(combinations(chicken, m))
for comb in combinations:
    dist = 0
    for a, b in house:
        tmp = n * 2
        for x, y in comb:
            tmp = min(tmp, abs(a - x) + abs(b - y))
        dist += tmp
    answer = min(answer, dist)

print(answer)