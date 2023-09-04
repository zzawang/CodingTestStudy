from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def cheese(a, b):
    q = deque([(a, b)])
    visited[a][b] = True
    melt = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if arr[nx][ny] == '1':
                    melt.append((nx, ny))
                elif arr[nx][ny] == '0':
                    q.append((nx, ny))

    for m1, m2 in melt:
        arr[m1][m2] = 'C'

    return True if len(melt) > 0 else False

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline().split()))

count1 = 0
while True:
    visited = [[False]*M for _ in range(N)]
    # 녹는 치즈 탐색
    check = cheese(0, 0)
    if not check:
        break
    count2 = 0

    for i1 in range(N):
        for i2 in range(M):
            if arr[i1][i2] == 'C':
                count2 += 1
                arr[i1][i2] = '0'

    count1 += 1

print(count1)
print(count2)