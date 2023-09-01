from collections import deque
import sys
def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    # 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없으므로 물 먼저 q에 삽입
    for w in water:
        q.append(w)
    q.append(start) # 고슴도치 위치 삽입

    while q:
        x, y = q.popleft()
        if (x, y) == arrive:
            return visited[x][y] - 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and arr[nx][ny] != '*' and arr[nx][ny] != 'X':
                if arr[x][y] == '*':
                    # 물은 비버 굴로 갈 수 없다.
                    if arr[nx][ny] == 'D':
                        continue
                    arr[nx][ny] = '*'
                else:
                    arr[nx][ny] = 'S'
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return "KAKTUS"

r, c = map(int, input().split())
visited = [[0]*c for _ in range(r)]
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline()))

# 고슴도치와 물이 있는 위치 먼저 파악
water = []
start = ()
arrive = ()
for i1 in range(r):
    for i2 in range(c):
        if arr[i1][i2] == '*':
            water.append((i1, i2))
            visited[i1][i2] = 1
        elif arr[i1][i2] == 'S':
            start = (i1, i2)
            visited[i1][i2] = 1
        elif arr[i1][i2] == 'D':
            arrive = (i1, i2)

print(bfs())