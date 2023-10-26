for tc in range(1, int(input()) + 1):
    arr = [x for x in input()]
    a, b = 1, 1
    for ar in arr:
        if ar == 'L':
            a, b = a, a+b
        else:
            a, b = a+b, b

    print(f"#{tc} {a} {b}")