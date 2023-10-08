for test_case in range(1, int(input()) + 1):
    a, b, c, d = map(int, input().split())
    m = (b+d)%60
    h = ((b+d)//60 + a + c)%12
    if h == 0:
        h = 12
    print(f"#{test_case} {h} {m}")