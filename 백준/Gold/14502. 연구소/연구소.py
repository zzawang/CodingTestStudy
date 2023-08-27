from collections import deque
from itertools import combinations
import copy
import sys

def bfs(maps, N, M):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False]*M for _ in range(N)]

    # 탐색 시작점 찾기
    for i1 in range(N):
        for i2 in range(M):
            if maps[i1][i2] == 2:
                q = deque([(i1, i2)])
                visited[i1][i2] = True

                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] == 0:
                            visited[nx][ny] = True
                            maps[nx][ny] = 2
                            q.append((nx, ny))

    count = 0
    for i1 in range(N):
        for i2 in range(M):
            if  maps[i1][i2] == 0:
                count += 1

    return count

def main():
    N, M = map(int, sys.stdin.readline().split())
    answer = []
    zero = []
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i1 in range(N):
        for i2 in range(M):
            if arr[i1][i2] == 0:
                zero.append((i1, i2))

    # 벽이 들어갈 수 있는 경우의 수
    result = list(combinations(zero, 3))
    for li in result:
        maps = copy.deepcopy(arr)
        for tup in li:
            a, b = tup
            maps[a][b] = 1

        answer.append(bfs(maps, N, M))

    print(max(answer))

main()