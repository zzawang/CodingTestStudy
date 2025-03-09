import sys

answer = 0
home = ()

def back_tracking(start, hp, milk):
    global answer, home
    x, y = start
    hx, hy = home

    for nx, ny in milks:
        if village[nx][ny] == 2:  # 아직 안마신 우유라면
            distance = abs(nx - x) + abs(ny - y)  # 다음 우유와 현재 위치와의 거리
            if distance <= hp:
                village[nx][ny] = 0
                back_tracking((nx, ny), hp - distance + H, milk + 1)
                village[nx][ny] = 2

    # 현재 위치에서 집까지 복귀할 힘이 남았는지 검사
    if abs(hx - x) + abs(hy - y) <= hp:
        answer = max(answer, milk)


# 민초마을의 크기인 N과 진우의 초기체력 M, 그리고 민트초코우유를 마실때 마다 증가하는 체력의 양 H
N, M, H = map(int, sys.stdin.readline().rstrip().split())
village = []
for _ in range(N):
    village.append(list(map(int, sys.stdin.readline().rstrip().split())))

milks = []
for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            home = (i, j)
        elif village[i][j] == 2:
            milks.append((i, j))

back_tracking(home, M, 0)  # 진우의 집에서 백트래킹 시작
print(answer)