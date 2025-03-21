import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

loops = min(N, M) // 2
for i in range(loops):
    q = deque()
    for j in range(i, M - i):
        q.append(arr[i][j])
    for k in range(i + 1, N - i - 1):
        q.append(arr[k][M - i - 1])
    for l in range(M - i - 1, i - 1, -1):
        q.append(arr[N - i - 1][l])
    for m in range(N - i - 2, i, -1):
        q.append(arr[m][i])

    if q:
        q.rotate(-R)
        for j in range(i, M - i):
            arr[i][j] = q.popleft()
        for k in range(i + 1, N - i - 1):
            arr[k][M - i - 1] = q.popleft()
        for l in range(M - i - 1, i - 1, -1):
            arr[N - i - 1][l] = q.popleft()
        for m in range(N - i - 2, i, -1):
            arr[m][i] = q.popleft()

for a in arr:
    print(*a)