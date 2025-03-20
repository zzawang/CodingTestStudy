import sys
from collections import defaultdict
from collections import deque


N, M, K, X = map(int, sys.stdin.readline().rstrip().split())
cities = defaultdict(list)

for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().rstrip().split())
    cities[c1].append(c2)


visited = [-1] * (N + 1)
visited[X] = 0
q = deque([(X, 0)])  # 현재 도시, 최단 거리

while q:
    city, distance = q.popleft()
    for c in cities[city]:
        if visited[c] == -1:
            visited[c] = distance + 1
            q.append((c, distance + 1))

answer = []
check = 0
for idx, r in enumerate(visited):
    if r == K:
        print(idx)
        check += 1

if check == 0:
    print(-1)