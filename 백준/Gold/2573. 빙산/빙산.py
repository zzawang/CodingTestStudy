from collections import deque
import sys
def bfs(i1, i2):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque([(i1, i2)])
    visited[i1][i2] = True
    change = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    sea += 1
                elif arr[nx][ny] > 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

        if sea > 0:
            change.append((x, y, sea))

    for a, b, s in change:
        arr[a][b] -= s
        if arr[a][b] < 0:
            arr[a][b] = 0

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = 0

while True:
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i1 in range(n):
        for i2 in range(m):
            if arr[i1][i2] != 0 and not visited[i1][i2]:
                bfs(i1, i2)
                count += 1

    answer += 1
    if count == 0:
        answer = 0
        break
    elif count > 1:
        answer -= 1
        break

print(answer)