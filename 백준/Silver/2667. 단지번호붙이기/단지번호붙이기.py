from collections import deque

def bfs(N, visited, map, start):
    count = 1
    q = deque([start])
    visited[start[0]][start[1]] = True
    # 동서남북
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        # 현재 위치
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and map[nx][ny] == '1':
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    return count

N = int(input())
visited = [[False] * N for _ in range(N)]
map = []
answer = []

for _ in range(N):
    map.append(input())

for i1 in range(N):
    for i2 in range(N):
        # 아직 방문하지 않았고 1이라면 집 탐색 시작
        if not visited[i1][i2] and map[i1][i2] == '1':
            # 탐색할 위치 bfs 시작
            answer.append(bfs(N, visited, map, (i1, i2)))

print(len(answer))
for x in sorted(answer):
    print(x)