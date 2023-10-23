def func(a, b):
    if b == 0:
        return 1
    else:
        return a*func(a, b-1)

for _ in range(1, 11):
    n = int(input())
    a, b = map(int, input().split())
    result = func(a, b)

    print(f"#{n} {result}")