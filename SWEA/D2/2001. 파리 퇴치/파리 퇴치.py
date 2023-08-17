def count(arr, x, y, m):
    sum = 0
    for x1 in range(x, x+m):
        for y1 in range(y, y+m):
            sum += arr[x1][y1]
    return sum

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    answer = []
    for i1 in range(n - m + 1):
        for i2 in range(n - m + 1):
            answer.append(count(arr, i1, i2, m))

    print(f"#{tc} {max(answer)}")