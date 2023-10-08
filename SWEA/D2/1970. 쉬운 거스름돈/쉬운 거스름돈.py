for test_case in range(1, int(input()) + 1):
    money = int(input())
    arr = []
    check = 50000
    for i in range(8):
        if i != 0 and i%2 == 0:
            check //= 2
        elif i%2 == 1:
            check //= 5

        arr.append(str(money // check))
        money %= check

    answer = " ".join(arr)
    print(f"#{test_case}\n{answer}")