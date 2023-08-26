from collections import deque
def bfs(i1, i2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(i1, i2)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and (nx, ny) != (0, 0):
                arr[nx][ny] += arr[x][y]
                q.append((nx, ny))


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(int(x) for x in input()))

bfs(0, 0)
print(arr[n-1][m-1])