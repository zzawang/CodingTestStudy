from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_pos(likes, classroom):
    start = []
    for i1 in range(N):
        for i2 in range(N):
            if classroom[i1][i2] == 0: # 자리가 비어있으면
                start.append((i1, i2))

    q = deque(start)
    visited = []

    while q:
        x, y = q.popleft()
        count = 0
        empty = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if classroom[nx][ny] in likes:
                    count += 1
                if classroom[nx][ny] == 0:
                    empty += 1

        visited.append((x, y, count, empty))


    # y가 작은 순서대로
    visited.sort(key=lambda x: x[1])

    # x가 작은 순서대로
    visited.sort(key=lambda x: x[0])

    # empty가 큰 순서대로
    visited.sort(key=lambda x: x[3], reverse=True)

    # count가 큰 순서대로
    visited.sort(key=lambda x:x[2], reverse=True)

    return (visited[0][0], visited[0][1])


def calculate_satisfaction(x, y, classroom):
    student = classroom[i1][i2]
    likes = student_likes[student]  # 학생이 좋아하는 4명의 학생들

    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if classroom[nx][ny] in likes:
                count += 1

    return count

N = int(sys.stdin.readline())

student_likes = {}  # 각 학생이 좋아하는 학생 4명의 번호
student_satisfaction = {}  # 각 학생의 만족도
student_sequence = [] # 학생이 삽입된 순서
satisfaction = [0, 1, 10, 100, 1000]

for _ in range(N*N):
    s = list(map(int, sys.stdin.readline().split()))
    student_likes[s[0]] = s[1:]
    student_sequence.append(s[0])
    student_satisfaction[s[0]] = 0

classroom = [[0 for _ in range(N)] for _ in range(N)]

for student in student_sequence:
    likes = student_likes[student] # 학생이 좋아하는 4명의 학생들
    x, y = find_pos(likes, classroom) # 학생의 자리 찾기
    classroom[x][y] = student


for i1 in range(N):
    for i2 in range(N):
        student = classroom[i1][i2]
        student_satisfaction[student] = calculate_satisfaction(i1, i2, classroom)  # 학생의 만족도 구하기

satisfaction_sum = sum(satisfaction[satisfac] for satisfac in student_satisfaction.values())
print(satisfaction_sum)