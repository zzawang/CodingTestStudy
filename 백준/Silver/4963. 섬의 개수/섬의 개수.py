from collections import deque
def bfs(visited, island, i1, i2, h, w):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    q = deque([(i1, i2)])
    visited[i1][i2] = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and island[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    # 바다지도 만들기
    island = []
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        island.append(list(map(int, input().split())))

    answer = 0
    for i1 in range(h):
        for i2 in range(w):
            # 아직 방문하지 않은 섬이 있다면 bfs로 탐색
            if not visited[i1][i2] and island[i1][i2] == 1:
                bfs(visited, island, i1, i2, h, w)
                answer += 1

    print(answer)