from collections import deque

def dfs(visited, n, start):
    print(start, end = ' ')
    visited[start] = True

    for n1 in sorted(n[start]):
        if visited[n1] == False:
            dfs(visited, n, n1)

def bfs(visited, q):
    while q:
        s = q.popleft()
        visited[s] = True
        print(s, end=' ')
        for s1 in sorted(n[s]):
            if visited[s1] == False:
                q.append(s1)
                visited[s1] = True

N, V, start = map(int, input().split())
n = [[] for _ in range(N+1)]

for v in range(V):
    a, b = map(int, input().split())
    if b not in n[a]:
        n[a].append(b)
        n[b].append(a)

dfs([False]*(N+1), n, start)
print()
q = deque()
q.append(start)
bfs([False]*(N+1), q)