T = int(input())
for t in range(1, T + 1):
    find = set()
    n = int(input())
    index = 0
    while len(find) != 10:
        index += 1
        k = set(str(n * index))
        for k1 in k:
            if k1 not in find:
                find.add(k1)
    print(f"#{t} {n * index}")