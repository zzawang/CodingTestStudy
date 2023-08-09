for tc in range(1, int (input()) + 1):
    distance = 0
    acc = 0
    for _ in range(int(input())):
        str = input()
        if str[0] == '0':
            distance += acc
        else:
            c, v = map(int, str.split())
            if c == 1:
                acc += v
                distance += acc
            else:
                acc -= v
                if acc < 0:
                    acc = 0
                distance += acc

    print(f"#{tc} {distance}")