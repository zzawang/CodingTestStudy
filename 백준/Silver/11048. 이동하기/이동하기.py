import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

result = [[0] * M for _ in range(N)]
result[0][0] = arr[0][0]
for x in range(1, N):
    result[x][0] = result[x - 1][0] + arr[x][0]

for y in range(1, M):
    result[0][y] = result[0][y - 1] + arr[0][y]

for i in range(1, N):
    for j in range(1, M):
        result[i][j] = arr[i][j] + max(result[i - 1][j - 1], result[i][j - 1], result[i - 1][j])

print(result[N - 1][M - 1])