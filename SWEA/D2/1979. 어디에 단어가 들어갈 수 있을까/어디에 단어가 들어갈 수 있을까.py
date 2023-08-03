for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    puzzle = []
    count = 0

    for _ in range(n):
        puzzle.append(list(map(int, input().split())))

    # 가로
    for i1 in range(n):
        check = 0
        for i2 in range(n):
            check = check + puzzle[i1][i2] if puzzle[i1][i2] == 1 else 0
            if check == k:
                if i2 + 1 == n or i2 + 1 < n and puzzle[i1][i2 + 1] == 0:
                    count += 1
                    check = 0

    # 세로
    for i1 in range(n):
        check = 0
        for i2 in range(n):
            check = check + puzzle[i2][i1] if puzzle[i2][i1] == 1 else 0
            if check == k:
                if i2 + 1 == n or i2 + 1 < n and puzzle[i2 + 1][i1] == 0:
                    count += 1
                    check = 0

    print(f"#{t} {count}")