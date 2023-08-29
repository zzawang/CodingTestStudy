from collections import deque
def bfs():
    dx = [2, 2, 1, 1, -2, -2, -1, -1]
    dy = [-1, 1, -2, 2, -1, 1, -2, 2]
    q = deque([(a, b)])

    while q:
        x, y = q.popleft()
        if (x, y) == (c, d):
            return arr[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

for tc in range(int(input())):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    arr = [[0]*l for _ in range(l)]
    print(bfs())