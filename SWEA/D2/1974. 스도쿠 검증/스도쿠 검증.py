for test_case in range(1, int(input()) + 1):
    flag = 1
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    # 가로 세로 확인
    for i1 in range(9):
        check1 = set()
        check2 = set()
        for i2 in range(9):
            check1.add(arr[i1][i2])
            check2.add(arr[i2][i1])

        if len(check1) != 9 or len(check2) != 9:
            flag = 0

    # 정사각형 확인
    for x, y in [(0,0), (3,0), (6,0), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
        check3 = set()
        for i1 in range(3):
            for i2 in range(3):
                check3.add(arr[x+i1][y+i2])

        if len(check3) != 9:
            flag = 0

    print(f"#{test_case} {flag}")