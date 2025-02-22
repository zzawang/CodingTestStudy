# from collections import deque

# def bfs(start):
#     visited = [False] * (n + 1)
#     visited[start] = True
#     q = deque([start])
#     answer = 0
#
#     while q:
#         computer = q.popleft()
#         for c in computers[computer]: # 네트워크 상에서 직접 연결되어 있는 컴퓨터 순회
#             if not visited[c]:
#                 visited[c] = True
#                 q.append(c)
#                 answer += 1
#
#     return answer

count = 0

def dfs(start, visited):
    global count
    visited[start] = True
    for c in computers[start]:
        if not visited[c]:
            count += 1
            dfs(c, visited)


n = int(input())
pairs = int(input())
computers = [[] for _ in range(n + 1)]

for _ in range(pairs):
    p1, p2 = map(int, input().split())
    computers[p1].append(p2)
    computers[p2].append(p1)

# print(bfs(1))
dfs(1, [False] * (n + 1))
print(count)
