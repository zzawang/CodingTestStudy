for test_case in range(1, int(input()) + 1):
    arr = sorted(list(map(int, input().split())))
    print(f"#{test_case} {round(sum(arr[1:len(arr)-1])/8)}")