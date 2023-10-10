import sys
from collections import deque

def check(num, b, pre):
    if 0 <= num - 1 < 4 and num - 1 != pre:
        if top_list[num - 1][2] != top_list[num][6]:
            check(num - 1, -b, num)
            top_list[num - 1].rotate(-b)
    if 0 <= num + 1 < 4 and num + 1 != pre:
        if top_list[num][2] != top_list[num + 1][6]:
            check(num + 1, -b, num)
            top_list[num + 1].rotate(-b)
    return

top_list = []
for _ in range(4):
    top_list.append(deque(map(int, sys.stdin.readline().strip())))

k = int(sys.stdin.readline())

rotate_list = []
for _ in range(k):
    rotate_list.append(list(map(int, sys.stdin.readline().split())))

for a, b in rotate_list:    # 회전시킨 톱니바퀴의 번호, 방향
    check(a - 1, b, -10)
    top_list[a - 1].rotate(b)

answer = top_list[0][0] * 1 + top_list[1][0] * 2 + top_list[2][0] * 4 + top_list[3][0] * 8
print(answer)