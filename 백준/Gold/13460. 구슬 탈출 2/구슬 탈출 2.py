from collections import deque
import sys
def move(a, b, mx, my):
    count = 0
    while arr[a+mx][b+my] != '#' and arr[a][b] != 'O':
        a += mx
        b += my
        count += 1
    return (a, b, count)

# 왼 오 아래 위
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    q = deque([(rx, ry, bx, by, 1)])
    visited[rx][ry][bx][by] = True

    while q:
        x1, y1, x2, y2, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nrx, nry, rcount = move(x1, y1, dx[i], dy[i])
            nbx, nby, bcount = move(x2, y2, dx[i], dy[i])

            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(d)
                return
            if (nrx, nry) == (nbx, nby):
                if rcount > bcount:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))

    print(-1)

N, M = map(int, sys.stdin.readline().split())
# 4개의 좌표값에 대한 방문 확인 배열
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
arr = []

# 빨간 구슬, 파란 구슬, 구멍의 위치 파악
rx, ry, bx, by = 0, 0, 0, 0
for i1 in range(N):
    arr.append(list(sys.stdin.readline()))
    for i2 in range(M):
        if arr[i1][i2] == 'R':
            arr[i1][i2] = '.'
            rx, ry = i1, i2
        elif arr[i1][i2] == 'B':
            arr[i1][i2] = '.'
            bx, by = i1, i2

bfs()