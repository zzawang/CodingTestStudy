import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

# 내구도
arr = deque(map(int, sys.stdin.readline().split()))
# 벨트 위 로봇
robot = deque([0]*n)

answer = 0
while arr.count(0) < k:
    answer += 1

    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    arr.rotate(1)
    robot.rotate(1)
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다
    robot[-1] = 0

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    for i in range(n-2, -1, -1):
        if robot[i] != 0 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i], robot[i+1] = robot[i+1], robot[i]
            arr[i + 1] -= 1
            
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다
    robot[-1] = 0

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[0] > 0 and robot[0] == 0:
        arr[0] -= 1
        robot[0] = 1

print(answer)