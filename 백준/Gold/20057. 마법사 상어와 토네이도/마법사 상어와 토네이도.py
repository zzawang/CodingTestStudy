# 서, 남, 동, 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def sand_spread(a, b, sand, out_sand, rate, n, y_sand):
    rs = int(y_sand*rate)
    if 0 <= a < n and 0 <= b < n:
        arr[a][b] += rs
    else:
        out_sand += rs

    sand -= rs

    return (sand, out_sand)


def sand_move(arr, n, x1, x2, index):
    # x의 위치
    x = (x1, x2)
    # y의 위치
    y = (x[0] + dx[index], x[1] + dy[index])
    # a의 위치
    a = (y[0] + dx[index], y[1] + dy[index])

    # 현재 모래 양, 모래
    sand = y_sand = arr[y[0]][y[1]]
    arr[y[0]][y[1]] = 0 # y 초기화
    out_sand = 0  # 밖으로 나간 모래

    sand, out_sand = sand_spread(x[0] + dx[(index+1)%4], x[1] + dy[(index+1)%4], sand, out_sand, 0.01, n, y_sand)
    sand, out_sand = sand_spread(x[0] + dx[(index+3)%4], x[1] + dy[(index+3)%4], sand, out_sand, 0.01, n, y_sand)
    sand, out_sand = sand_spread(y[0] + dx[(index+1)%4], y[1] + dy[(index+1)%4], sand, out_sand, 0.07, n, y_sand)
    sand, out_sand = sand_spread(y[0] + dx[(index+3)%4], y[1] + dy[(index+3)%4], sand, out_sand, 0.07, n, y_sand)
    sand, out_sand = sand_spread(y[0] + dx[(index+1)%4]*2, y[1] + dy[(index+1)%4]*2, sand, out_sand, 0.02, n, y_sand)
    sand, out_sand = sand_spread(y[0] + dx[(index+3)%4]*2, y[1] + dy[(index+3)%4]*2, sand, out_sand, 0.02, n, y_sand)
    sand, out_sand = sand_spread(a[0] + dx[(index+1)%4], a[1] + dy[(index+1)%4], sand, out_sand, 0.1, n, y_sand)
    sand, out_sand = sand_spread(a[0] + dx[(index+3)%4], a[1] + dy[(index+3)%4], sand, out_sand, 0.1, n, y_sand)
    sand, out_sand = sand_spread(a[0] + dx[index], a[1] + dy[index], sand, out_sand, 0.05, n, y_sand)


    if 0 <= a[0] < n and 0 <= a[1] < n:
        arr[a[0]][a[1]] += sand
    else:
        out_sand += sand

    return out_sand


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dest = [x1 for x1 in range(1, n) for _ in range(2)] + [n]

start = (n//2, n//2) # 토네이도의 위치
index = 0
answer = 0 # 격자의 밖으로 나간 모래의 양
for d in dest:
    for _ in range(d):
        # 비율이 적혀 있는 칸으로 이동하고 α에는 남은 모래의 양이 더해짐
        # 이때 격자의 밖으로 나간 모래가 있으면 더해준다.
        answer += sand_move(arr, n, start[0], start[1], index)

        # 토네이도가 도착한 위치 == y의 위치
        nx = start[0] + dx[index]
        ny = start[1] + dy[index]
        start = (nx, ny)

    index = (index + 1)%4

print(answer)