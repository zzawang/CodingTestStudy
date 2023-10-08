for test_case in range(1, int(input()) + 1):
    n = int(input())
    price = list(map(int, input().split()))

    result = 0
    max_num = 0
    for i in range(len(price) - 1, -1, -1):
        if price[i] > max_num:
            max_num = price[i]
        else:
            result += max_num - price[i]

    print(f"#{test_case} {result}")