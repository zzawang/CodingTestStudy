import sys
from collections import deque
def bfs(node, visited, start, answer):
    q = deque([start])
    visited[start] = True
    while q:
        s = q.popleft()
        for x in node[s]:
            if not visited[x]:
                visited[x] = True
                answer[x] = s
                q.append(x)

n = int(input())
answer = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
node = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    if b not in node[a]:
        node[a].append(b)
        node[b].append(a)

for start in range(1, n+1):
    if not visited[start]:
        bfs(node, visited, start, answer)

for i in range(2, n+1):
    print(answer[i])