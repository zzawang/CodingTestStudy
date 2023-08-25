import sys
from collections import deque
def bfs(area, n, m, tomato):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    for t in tomato:
        q.append(t)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
                area[nx][ny] += (area[x][y] + 1)
                q.append((nx, ny))

def main():
    m, n = map(int, input().split())
    tomato = []
    area = []
    for i in range(n):
        area.append(list(map(int, sys.stdin.readline().split())))

    for i1 in range(n):
        for i2 in range(m):
            if area[i1][i2] == 1:
                tomato.append((i1, i2))

    bfs(area, n, m, tomato)

    mx = 0
    for i1 in range(n):
        for i2 in range(m):
            if area[i1][i2] == 0:
                print(-1)
                return
            elif area[i1][i2] > mx:
                mx = area[i1][i2]

    print(mx-1)

main()