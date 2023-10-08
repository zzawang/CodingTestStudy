for test_case in range(1, int(input()) + 1):
    n = int(input())
    text = ''
    for _ in range(n):
        a, b = input().split()
        text += a*int(b)

    print(f"#{test_case}")
    for i in range(len(text)):
        if i%10 == 0 and i != 0:
            print()
        print(text[i], end='')
    print()