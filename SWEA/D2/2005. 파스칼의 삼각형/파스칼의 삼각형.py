for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    arr[0][0] = 1
    for i1 in range(1, n):
        for i2 in range(n):
            if i2 == 0:
                arr[i1][i2] = 1
            else:
                arr[i1][i2] = arr[i1 - 1][i2 - 1] + arr[i1 - 1][i2]

    print(f"#{test_case}")
    for a1 in arr:
        for a2 in a1:
            if a2 != 0:
                print(a2, end=' ')
        print()