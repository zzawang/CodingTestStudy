T = int(input())
for t in range(1, T + 1):
    find = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = int(input())
    index = 0
    while find != []:
        index += 1
        k = list(map(int, str((n * index))))
        for k1 in k:
            if k1 in find:
                find.remove(k1)
    print(f"#{t} {n * index}")