import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True

    for node in nodes[start]:
        if not visited[node]:
            parents[node] = start
            dfs(node)

n = int(input())
visited = [False] * (n + 1)
nodes = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

dfs(1)

for i in range(2, n + 1):
    print(parents[i])
