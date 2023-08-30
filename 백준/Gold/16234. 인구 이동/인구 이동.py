from collections import deque

def bfs(i1, i2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(i1, i2)])
    area = [(i1, i2)]
    sum = arr[i1][i2]
    visited[i1][i2] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                q.append((nx, ny))
                area.append((nx, ny))
                sum += arr[nx][ny]
                visited[nx][ny] = True

    for a, b in area:
        arr[a][b] = sum//len(area)

    return len(area)

n, l, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
answer = 0
while True:
    # 이 부분이 중요. visited와 flag가 초기화되어야 함
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i1 in range(n):
        for i2 in range(n):
            if not visited[i1][i2]:
                if bfs(i1, i2) > 1:
                    flag = True

    if not flag:
        break
    answer += 1

print(answer)