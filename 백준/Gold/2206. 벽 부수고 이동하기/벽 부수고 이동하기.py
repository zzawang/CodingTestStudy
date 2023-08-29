from collections import deque
def bfs(arr, n, m):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if (x, y) == (n-1, m-1):
            return visited[x][y][wall]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                # 벽이 아니라면 이동
                if arr[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
                # 벽인데 아직 벽을 안부쉈다면
                elif wall == 0 and arr[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    q.append((nx, ny, 1))

    return -1

def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input())))

    print(bfs(arr, n, m))

main()