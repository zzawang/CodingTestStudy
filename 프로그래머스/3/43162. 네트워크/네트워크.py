def solution(n, computers):
    visited = [False for _ in range(n)] # 노드 방문 여부를 저장
    answer = 0
    
    for index in range(n):
        if not visited[index]: # 아직 방문하지 않은 노드라면
            dfs(n, computers, index, visited)
            answer += 1
    return answer

def dfs(n, computers, index, visited):
    visited[index] = True
    for new_index in range(n): # 노드와 연결된 다른 노드들을 DFS로 탐색
        if new_index != index and computers[index][new_index] == 1 and not visited[new_index]:
            dfs(n, computers, new_index, visited) # 연결된 노드들과 연결된 다른 노드들 재귀적으로 탐색