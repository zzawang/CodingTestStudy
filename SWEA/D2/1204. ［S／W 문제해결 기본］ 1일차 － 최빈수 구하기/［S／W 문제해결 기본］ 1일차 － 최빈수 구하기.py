for test_case in range(1, int(input()) + 1):
    n = int(input())
    num = [0]*101
    arr = list(map(int, input().split()))

    for a in arr:
        num[a] += 1

    max_num = max(num)
    for a in range(100, -1, -1):
        if num[a] == max_num:
            max_num = a
            break

    print(f"#{n} {max_num}")