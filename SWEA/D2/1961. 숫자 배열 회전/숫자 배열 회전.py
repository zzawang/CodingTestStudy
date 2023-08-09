for tc in range(1, int (input()) + 1):
    arr, a, b, c = [], [], [], []
    N = int(input())
    for _ in range(N):
        arr.append(list(input().split()))
    for i1 in zip(*arr):
        a.append(list(reversed([x1 for x1 in i1])))
    for i2 in zip(*a):
        b.append(list(reversed([x2 for x2 in i2])))
    for i3 in zip(*b):
        c.append(list(reversed([x3 for x3 in i3])))
    print(f"#{tc}")
    for i in range(N):
        print("".join(a[i]), end = " ")
        print("".join(b[i]), end=" ")
        print("".join(c[i]))