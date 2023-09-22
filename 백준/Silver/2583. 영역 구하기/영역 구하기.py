from collections import deque
import sys

def bfs(i1, i2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    q = deque([(i1, i2)])
    arr[i1][i2] = -1  # 방문 처리는 -1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                count += 1
                arr[nx][ny] = -1
                q.append((nx, ny))

    return count

M, N, K = map(int, sys.stdin.readline().split())
arr = [[0]*N for _ in range(M)]
answer = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i1 in range(M - y2, M - y1):
        for i2 in range(x1, x2):
            arr[i1][i2] = 1

for i1 in range(M):
    for i2 in range(N):
        if arr[i1][i2] == 0:
            answer.append(bfs(i1, i2))

print(len(answer))
for a in sorted(answer):
    print(a, end=' ')