from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(n, m, maps, visited):
    q = deque([(0, 0)])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    bfs(n, m, maps, visited)
    
    return visited[n - 1][m - 1] if visited[n - 1][m - 1] != 0 else -1