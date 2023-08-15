for tc in range(1, int(input()) + 1):
    n = int(input())
    print(f"#{tc}")
    if n == 1:
        print('1')
        continue
    arr = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, -1
    num = 0
    index = -1

    while arr[x + dx[(index + 1)%4]][y + dy[(index + 1)%4]] == 0:
        index = (index + 1)%4
        while 0 <= x + dx[index] < n and 0 <= y + dy[index] < n and arr[x + dx[index]][y + dy[index]] == 0:
            num += 1
            x += dx[index]
            y += dy[index]
            arr[x][y] = num

    for a1 in arr:
        for a2 in a1:
            print(a2, end=' ')
        print()