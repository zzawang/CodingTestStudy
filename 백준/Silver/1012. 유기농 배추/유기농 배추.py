from collections import deque
def bfs(arr, visited, x, y, n, m):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        a, b = q.popleft()
        for i in range(4):
            na, nb = a+dx[i], b+dy[i]
            # 아직 방문하지 않았는데 배추가 심어져 있다면
            if 0 <= na < n and 0 <= nb < m and not visited[na][nb] and arr[na][nb] == 1:
                q.append((na, nb))
                visited[na][nb] = True


for tc in range(int(input())):
    answer = 0
    m, n, k = map(int, input().split())
    # 방문 처리
    visited = [[False]*m for _ in range(n)]
    # 배추가 심어져 있는 땅
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for a1 in range(n):
        for a2 in range(m):
            # 아직 방문하지 않았는데 배추가 심어져 있다면
            if not visited[a1][a2] and arr[a1][a2] == 1:
                bfs(arr, visited, a1, a2, n, m)
                answer += 1

    print(answer)