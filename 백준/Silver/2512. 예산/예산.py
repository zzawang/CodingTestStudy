import sys

N = int(sys.stdin.readline().rstrip())  # 지방의 수
budgets = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())  # 총 예산
answer = 0
start, end = 1, max(budgets)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for b in budgets:
        if mid - b >= 0:
            tmp += b
        else:
            tmp += mid

    if tmp > M:  # 정해진 예산을 초과하면
        end = mid - 1
    else:
        start = mid + 1

print(end)
