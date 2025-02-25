import sys

n = int(sys.stdin.readline())
machines = sorted(list(map(int, sys.stdin.readline().split())))


if n % 2 == 0:
    answer = -1
    for i in range(n // 2):
        answer = max(answer, machines[i] + machines[n - i - 1])

else:
    answer = machines[-1]
    for i in range(n // 2):
        answer = max(answer, machines[i] + machines[n - i - 2])

print(answer)