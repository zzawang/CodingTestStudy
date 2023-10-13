import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def gravity(arr, n):
    for i2 in range(n):
        count = 0
        for i1 in range(n-1, -1, -1):
            if arr[i1][i2] == -1:
                count = 0
            elif arr[i1][i2] < -1:
                count += 1
            elif count > 0 and arr[i1][i2] >= 0:
                index = i1 + count
                arr[i1][i2], arr[index][i2] = arr[index][i2], arr[i1][i2]

    return arr

def rotate(arr, n):
    new_arr = []
    for i2 in range(n-1, -1, -1):
        array = []
        for i1 in range(n):
            array.append(arr[i1][i2])
        new_arr.append(array)
    return new_arr

def bfs(arr, visited, n, i1, i2):
    # (시작행, 시작열)
    q = deque([(i1, i2)])
    visited[i1][i2] = 1

    color_check = arr[i1][i2]
    blocks, rainbows = 0, 0
    block_group = []
    rainbow = []

    while q:
        x, y = q.popleft()
        block_group.append((x, y))
        blocks += 1
        # 기준 블록 찾기
        if arr[x][y] == 0:
            rainbows += 1
            rainbow.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and (arr[nx][ny] == color_check or arr[nx][ny] == 0):
                visited[nx][ny] = 1
                q.append((nx, ny))

    for a, b in rainbow:
        visited[a][b] = 0
    
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
    block_group.sort(key=lambda x:(x[0], x[1]))
    for a, b in block_group:
        if arr[a][b] != 0:
            xx, yy = a, b
            break

    # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 한다.
    if blocks < 2:
        return ()
    else:
        return (blocks, rainbows, xx, yy, block_group)

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

score = 0
# 크기가 가장 큰 블록 그룹이 존재하는 동안 계속해서 반복
while True:
    block_group_list = []
    visited = [[0] * n for _ in range(n)]
    for i1 in range(n):
        for i2 in range(n):
            if arr[i1][i2] > 0 and visited[i1][i2] == 0:
                block_array = bfs(arr, visited, n, i1, i2)
                if block_array != ():
                    block_group_list.append(block_array)

    if not block_group_list:
        break

    # 크기가 가장 큰 블록 그룹을 찾는다. 
    block_group_list.sort(key=lambda x : (-x[0], -x[1], -x[2], -x[3]))

    # 1에서 찾은 블록 그룹의 모든 블록을 제거하고, 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
    for a, b in block_group_list[0][4]:
        arr[a][b] = -1e9
    score += (block_group_list[0][0])**2

    arr = gravity(arr, n)
    arr = rotate(arr, n)
    arr = gravity(arr, n)

print(score)