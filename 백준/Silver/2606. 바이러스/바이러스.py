from collections import deque
def dfs(arr, visited, n, start):
    visited[start] = True
    arr.append(start)
    for i in sorted(n[start]):
        if not visited[i]:
            dfs(arr, visited, n, i)

def bfs(arr, visited, n, start):
    q = deque([start])
    visited[start] = True
    while q:
        i = q.popleft()
        visited[i] = True
        arr.append(i)
        for i1 in sorted(n[i]):
            if not visited[i1]:
                q.append(i1)
                visited[i1] = True

N = int(input())
V = int(input())

n = [[] for _ in range(N+1)]
for i in range(V):
    a, b = map(int, input().split())
    if b not in n[a]:
        n[a].append(b)
        n[b].append(a)

# arr1 = []
# dfs(arr1, [False]*(N+1), n, 1)
# print(len(arr1)-1)

arr2 = []
bfs(arr2, [False]*(N+1), n, 1)
print(len(arr2)-1)