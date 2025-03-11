import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def is_available(comb):
    visited = [[False] * 5 for _ in range(5)]
    must_visit = [[False] * 5 for _ in range(5)]
    s_count = 0
    for x, y in comb:
        if students[x][y] == 'S':
            s_count += 1
        must_visit[x][y] = True

    if s_count < 4:
        return False

    count = 0
    sx, sy = comb[0]
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()
        if must_visit[x][y]:
            count += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and must_visit[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    if count == 7:
        return True
    else:
        return False


answer = 0

def find_princess(n, comb):
    global answer

    if len(comb) == 7:
        if is_available(comb):
            answer += 1
        return

    for i in range(n, 25):
        nx, ny = i // 5, i % 5
        comb.append((nx, ny))
        find_princess(i + 1, comb)
        comb.pop()

students = []
for _ in range(5):
    students.append(sys.stdin.readline().rstrip())


find_princess(0, [])
print(answer)