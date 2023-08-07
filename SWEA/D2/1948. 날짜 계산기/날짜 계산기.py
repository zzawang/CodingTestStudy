days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, int (input()) + 1):
    m1, d1, m2, d2 = map(int, input().split())
    answer = d2

    for i in range(m1, m2):
        answer += days[i]

    answer = answer - d1 + 1

    print(f"#{tc} {answer}")