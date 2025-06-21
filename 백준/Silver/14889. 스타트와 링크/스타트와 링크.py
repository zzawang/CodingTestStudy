import sys

n = int(sys.stdin.readline())
status = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [False] * n
result = sys.maxsize

def dfs(depth, idx):
    global result

    if depth == n // 2:
        team_start = 0
        team_link = 0

        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    team_start += status[i][j] + status[j][i]
                elif not visited[i] and not visited[j]:
                    team_link += status[i][j] + status[j][i]

        result = min(result, abs(team_start - team_link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(result)
