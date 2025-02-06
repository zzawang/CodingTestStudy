n, x = map(int, input().split())
visitors = list(map(int, input().split()))

count = 0
max_count = -1
period = 0

for i, v in enumerate(visitors):
    count += v
    if i >= x - 1:
        if count > max_count:
            max_count = count
            period = 1
        elif count == max_count:
            period += 1
        count -= visitors[i - x + 1]

if max_count == 0:
    print("SAD")
else:
    print(max_count)
    print(period)