import sys
from collections import deque
def bfs(boxes, M, N, H, que):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dh = [0, 0, 0, 0, -1, 1]
    q = deque()
    for num in que:
        q.append(num)

    while q:
        h, x, y = q.popleft()
        # 같은 층 탐색
        for i in range(6):
            nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and boxes[nh][nx][ny] == 0:
                boxes[nh][nx][ny] = boxes[h][x][y] + 1
                q.append((nh, nx, ny))

def main():
    M, N, H = map(int, input().split())
    boxes = []
    for _ in range(H):
        arr = []
        for _ in range(N):
            arr.append(list(map(int, sys.stdin.readline().split())))
        boxes.append(arr)

    que = []
    for h in range(H):
        for i1 in range(N):
            for i2 in range(M):
                if boxes[h][i1][i2] == 1:
                    que.append((h, i1, i2))

    bfs(boxes, M, N, H, que)

    answer = 0
    for box in boxes:
        for b1 in box:
            for b2 in b1:
                if b2 == 0:
                    print(-1)
                    return
                elif b2 > answer:
                    answer = b2

    print(answer-1)

main()