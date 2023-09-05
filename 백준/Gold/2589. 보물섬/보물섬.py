from collections import deque
import sys
def bfs(a, b):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0] * M for _ in range(N)]
    q = deque([(a, b, 0)])
    visited[a][b] = True

    max_num = []
    while q:
        x, y, d = q.popleft()
        max_num.append(d)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 'L':
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))

    return max(max_num)

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

max_count = []
for i1 in range(N):
    for i2 in range(M):
        # 위아래가 육지인 경우
        if 0 <= i1 - 1 < N and 0 <= i1 + 1 < N and arr[i1 - 1][i2] == 'L' and arr[i1 + 1][i2] == 'L':
            continue
        # 양옆이 육지인 경우
        if 0 <= i2 - 1 < M and 0 <= i2 + 1 < M and arr[i1][i2 - 1] == 'L' and arr[i1][i2 + 1] == 'L':
            continue
        if arr[i1][i2] == 'L':
            max_count.append(bfs(i1, i2))

print(max(max_count))