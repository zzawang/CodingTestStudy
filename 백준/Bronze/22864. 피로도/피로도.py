a, b, c, m = map(int, input().split())
status = 0
answer = 0

for _ in range(0, 24):
    if status + a > m:
        status -= c
        if status < 0:
            status = 0
    else:
        status += a
        answer += b

print(answer)