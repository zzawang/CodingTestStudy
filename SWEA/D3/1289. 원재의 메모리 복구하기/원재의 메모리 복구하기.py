for tc in range(1, int(input()) + 1):
    n = list(map(int, input()))

    answer = 0
    for i1 in range(len(n)):
        if n[i1] == 1:
            n[i1] = 0
            answer += 1
            for i2 in range(i1 + 1, len(n)):
                n[i2] = not n[i2]

    print(f"#{tc} {answer}")