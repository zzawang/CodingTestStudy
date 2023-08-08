T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(f"#{tc}", end = " ")
    for a in arr:
        print(a, end = " ")
    print()