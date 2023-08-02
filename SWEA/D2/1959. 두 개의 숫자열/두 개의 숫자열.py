T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mn = []
    mx = []
    if n > m:
        mx = a
        mn = b
    else:
        mx = b
        mn = a

    count = []
    sum = 0
    x = 0
    n = 0
    mv = 0

    while mv <= len(mx) - len(mn):

        sum += (mn[n] * mx[x])
        n += 1
        x += 1

        if n >= len(mn):
            n = 0
            x -= (len(mn) - 1)
            mv += 1
            count.append(sum)
            sum = 0

    print(f"#{t} {max(count)}")