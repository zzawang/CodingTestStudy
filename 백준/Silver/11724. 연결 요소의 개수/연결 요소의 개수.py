# def dfs(node, visited, a):
#     visited[a] = True
#     for i in node[a]:
#         if not visited[i]:
#             dfs(node, visited, i)
# 
# N, M = map(int, input().split())
# node = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# answer = 0
# 
# for _ in range(M):
#     a, b = map(int, input().split())
#     if b not in node[a]:
#         node[a].append(b)
# 
# for a in range(1, len(node)):
#     if not visited[a]:  # 아직 노드 a를 방문하지 않았다면
#         dfs(node, visited, a)   # 노드 a에 연결된 노드들을 탐색
#         answer += 1
# 
# print(answer)


from collections import deque
def bfs(node, visited, a):
    q = deque([a])
    visited[a] = True
    
    while q:
        s = q.popleft()
        for i in node[s]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for a in range(1, len(node)):
    if not visited[a]:  # 아직 노드 a를 방문하지 않았다면
        bfs(node, visited, a)   # 노드 a에 연결된 노드들을 탐색
        answer += 1

print(answer)