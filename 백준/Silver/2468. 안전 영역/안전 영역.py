from collections import deque
def bfs(area, visited, i1, i2, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(i1, i2)])
    visited[i1][i2] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] >= m:
                visited[nx][ny] = True
                q.append((nx, ny))

def findMax(n, m, area):
    visited = [[False]*n for _ in range(n)]
    answer = 0

    for i1 in range(n):
        for i2 in range(n):
            if not visited[i1][i2] and area[i1][i2] >= m:
                bfs(area, visited, i1, i2, n, m)
                answer += 1

    return answer

n = int(input())
area = []
find = []
for _ in range(n):
    area.append(list(map(int, input().split())))

for i in range(1, 101):
    find.append(findMax(n, i, area))

print(max(find))