from collections import deque
def bfs(area, visited, n, m, tomato):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    for t in tomato:
        q.append(t)
        a, b = t
        visited[a][b] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and area[nx][ny] == 1:
                area[nx][ny] += area[x][y]
                visited[nx][ny] = True
                q.append((nx, ny))

def main():
    m, n = map(int, input().split())
    tomato = []
    area = []
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        area.append(list(map(int, input().split())))

    for i1 in range(n):
        for i2 in range(m):
            if area[i1][i2] == 1:
                tomato.append((i1, i2))
            elif area[i1][i2] == 0:
                area[i1][i2] = 1

    bfs(area, visited, n, m, tomato)
    
    mx = 0
    for i1 in range(n):
        for i2 in range(m):
            if not visited[i1][i2] and area[i1][i2] == 1:
                print(-1)
                return
            elif area[i1][i2] > mx:
                mx = area[i1][i2]

    print(mx-1)

main()