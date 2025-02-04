import sys

n = int(input())
answer = sys.maxsize

for i in range(n // 5 + 1):
    tmp = n - 5 * i
    if tmp % 2 == 0:
        answer = min(answer, i + tmp // 2)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)