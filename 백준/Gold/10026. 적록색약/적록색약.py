from collections import deque
def bfs1(visited1, arr, i1, i2, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(i1, i2)])
    visited1[i1][i2] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited1[nx][ny] and arr[nx][ny] == arr[i1][i2]:
                visited1[nx][ny] = True
                q.append((nx, ny))

def bfs2(visited2, arr, i1, i2, N, M):
    if arr[i1][i2] == 'B':
        check = 'B'
    else:
        check = "RG"
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(i1, i2)])
    visited2[i1][i2] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited2[nx][ny] and arr[nx][ny] in check:
                visited2[nx][ny] = True
                q.append((nx, ny))


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))
M = len(arr[0])

# 일반 사람
visited1 = [[False for _ in range(M)] for _ in range(N)]
answer1 = 0

# 색맹
visited2 = [[False for _ in range(M)] for _ in range(N)]
answer2 = 0

for i1 in range(N):
    for i2 in range(M):
        if not visited1[i1][i2]:
            bfs1(visited1, arr, i1, i2, N, M)
            answer1 += 1
        if not visited2[i1][i2]:
            bfs2(visited2, arr, i1, i2, N, M)
            answer2 += 1

print(answer1, answer2)