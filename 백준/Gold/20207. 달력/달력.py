import sys

N = int(sys.stdin.readline().rstrip())
days = [0] * 366
for _ in range(N):
    d1, d2 = map(int, sys.stdin.readline().rstrip().split())
    for idx in range(d1, d2 + 1):
        days[idx] += 1

answer = 0
row = 0  # 가로 길이
col = 0  # 세로 길이
for i in range(1, 366):
    if days[i] == 0:  # 일정이 없는 경우
        answer += (row * col)
        row = 0
        col = 0
    else:
        row += 1
        col = max(col, days[i])

answer += (row * col) # 마지막 남은 일정들 더해주기
print(answer)