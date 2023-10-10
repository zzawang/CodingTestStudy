import sys
dx1 = [0, -1, -1, -1, 0, 1, 1, 1]
dy1 = [-1, -1, 0, 1, 1, 1, 0, -1]
dx2 = [1, 1, -1, -1]
dy2 = [-1, 1, 1, -1]

def bfs(clouds, arr, n, d, s):
    # 구름의 위치
    # 구름이 있는 위치를 확인하고 d방향으로 s칸 이동
    new_clouds = []
    for i1, i2 in clouds:
        ni1 = (i1 + dx1[d-1]*s)%n
        if ni1 < 0:
            ni1 += n
        ni2 = (i2 + dy1[d-1]*s)%n
        if ni2 < 0:
            ni2 += n
        arr[ni1][ni2] += 1
        new_clouds.append((ni1, ni2))   # 마지막에 구름이 있던 위치

    clouds = new_clouds
    counts = []
    for a, b in clouds:
        count = 0
        for i in range(4):
            na, nb = a + dx2[i], b + dy2[i]
            if 0 <= na < n and  0 <= nb < n and arr[na][nb] != 0:
                count += 1

        counts.append((count))

    for length in range(len(clouds)):
        a, b = clouds[length]
        arr[a][b] += counts[length]

    new_clouds = []
    check = [[False]*n for _ in range(n)]
    for a, b in clouds:
        check[a][b] = True

    for i1 in range(n):
        for i2 in range(n):
            if arr[i1][i2] >= 2 and not check[i1][i2]:
                new_clouds.append((i1, i2))
                arr[i1][i2] -= 2

    return new_clouds

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    # 첫 비바라기 시전
    clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

    for _ in range(m):
        d, s = map(int, sys.stdin.readline().split())
        clouds = bfs(clouds, arr, n, d, s)

    answer = 0
    for a in arr:
        answer += sum(a)
    print(answer)

main()