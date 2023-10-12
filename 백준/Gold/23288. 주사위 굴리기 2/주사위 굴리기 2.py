import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(arr, dice, n, m):
    a, b = dice
    score = arr[a][b]
    q = deque([dice])
    visited = [[False]*m for _ in range(n)]
    visited[a][b] = True

    count = 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == score:
            count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == score:
                visited[nx][ny] = True
                q.append((nx, ny))

    return count * score

# 회전
def rotate_dice(dice_list1, dice_list2, r_num):
    # 동
    if r_num == 0:
        dice_list1.rotate(1)
        dice_list2[1] = dice_list1[1]
        dice_list1[0], dice_list2[-1] = dice_list2[-1], dice_list1[0]
    # 남
    elif r_num == 1:
        dice_list2.rotate(1)
        dice_list1[1] = dice_list2[1]
    # 서
    elif r_num == 2:
        dice_list1.rotate(-1)
        dice_list2[1] = dice_list1[1]
        dice_list1[-1], dice_list2[-1] = dice_list2[-1], dice_list1[-1]
    # 북
    else:
        dice_list2.rotate(-1)
        dice_list1[1] = dice_list2[1]

    return (dice_list1, dice_list2)

n, m, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 동, 남, 서, 북 (90도 시계 방향)
rotate = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r_num = 0 # 현재 회전 방향
dice_list1 = deque([4, 1, 3])  # 주사위 가로 배열
dice_list2 = deque([2, 1, 5, 6])  # 주사위 가로 배열

# 각 이동에서 획득하는 점수의 합
answer = 0
# 주사위의 현재 위치
dice = (0, 0)

# 이동 횟수
for i in range(k):
    # 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    x, y = dice[0] + rotate[r_num][0], dice[1] + rotate[r_num][1]
    if x < 0 or x >= n or y < 0 or y >= m :
        r_num = (r_num + 2) % 4

    dice = (dice[0] + rotate[r_num][0], dice[1] + rotate[r_num][1])
    (dice_list1, dice_list2) = rotate_dice(dice_list1, dice_list2, r_num)

    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    answer += bfs(arr, dice, n, m)

    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    if dice_list2[-1] > arr[dice[0]][dice[1]]:
        r_num = (r_num + 1)%4
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    elif dice_list2[-1] < arr[dice[0]][dice[1]]:
        r_num = (r_num + 3)%4

print(answer)