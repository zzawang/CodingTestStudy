N = int(input())
meetings = []
answer = 0

for i in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort()
tmp = meetings[0]

for i in range(1, N):
    if tmp[1] <= meetings[i][0]:
        answer += 1
        tmp = meetings[i]
    elif tmp[1] > meetings[i][1]:
        tmp = meetings[i]

answer += 1
print(answer)