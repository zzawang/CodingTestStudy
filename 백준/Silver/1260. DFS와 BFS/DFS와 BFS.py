from collections import deque

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=' ')

        for linked_node in nodes[node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                q.append(linked_node)


def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')

    for node in nodes[start]:
        if not visited[node]:
            dfs(node, visited)


n, m, v = map(int, input().split())
nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

for node_arr in nodes:
    node_arr.sort()

dfs(v, [False] * (n + 1))
print()
bfs(v)
