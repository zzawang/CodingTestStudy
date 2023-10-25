def find():
    count = 0
    for i1 in range(8):
        for i2 in range(8 - n + 1):
            if list(arr[i1][i2: i2 + n//2]) == list(reversed(arr[i1][i2 + n//2 + n % 2: i2 + n])):
                count += 1

    return count

for tc in range(1, 11):
    n = int(input()) # 찾아야 하는 회문의 길이
    arr = []
    answer = 0
    for _ in range(8):
        arr.append([x for x in input()])

    answer += find()
    arr = list(zip(*arr))
    answer += find()

    print(f"#{tc} {answer}")