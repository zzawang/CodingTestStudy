import sys
from collections import deque
def bfs(babyshark):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque([babyshark])
    visited = [[0]*n for _ in range(n)]
    visited[babyshark[0]][babyshark[1]] = 1

    littlefish = []
    new_littlefish = []
    min_count = 1000000

    while q:
        x, y = q.popleft()
        if 0 < arr[x][y] <= sharksize - 1:
            littlefish.append((x, y))
            if min_count > visited[x][y]:
                min_count = visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] <= sharksize:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    for a, b in littlefish:
        if visited[a][b] == min_count:
            new_littlefish.append((a, b))

    return  (new_littlefish, visited)

n = int(sys.stdin.readline())
fish_list = {1 : [], 2: [], 3 : [], 4 : [], 5 : [], 6 : []}
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i1 in range(n):
    for i2 in range(n):
        if arr[i1][i2] == 9:
            babyshark = (i1, i2)
            arr[i1][i2] = 0

eatfish = 0
sharksize = 2
answer = 0
while True:
    littlefish, visited = bfs(babyshark)
    if len(littlefish) == 0:
        break
    else:
        littlefish.sort(key=lambda x: x[1])
        littlefish.sort(key=lambda x: x[0])
        a, b = littlefish[0]
        babyshark = (a, b)
        eatfish += 1
        arr[a][b] = 0
        answer += (visited[a][b] - 1)
        if eatfish == sharksize:
            sharksize += 1
            eatfish = 0

print(answer)