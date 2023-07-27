T = int(input())
for t in range(1, T + 1):
    sum = 0
    for i in range(1, int(input()) + 1):
        sum = sum + i if i%2 == 1 else sum - i
    print(f"#{t} {sum}")
