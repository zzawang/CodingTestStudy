from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(seats, likes, n, start):
    q = deque([])
    for s in start:
        q.append(s)

    arr = [[-1] * n for _ in range(n)]
    max = 0
    answer1 = []  # 1번 조건 만족
    answer2 = []  # 2번 조건 만족

    # 1번 조건
    while q:
        x, y = q.popleft()
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in likes:
                count += 1

        arr[x][y] = count
        if max < count:
            max = count

    for i1 in range(n):
        for i2 in range(n):
            if max == arr[i1][i2]:
                answer1.append((i1, i2))
            arr[i1][i2] = -1     # 재활용

    # 1번 조건을 만족하는 위치가 여러 개라면 2번 조건 체크
    if len(answer1) == 1:
        return answer1[0]
    else:
        max = 0
        for a in answer1:
            q.append(a)

        while q:
            x, y = q.popleft()
            count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] == '0':
                    count += 1

            arr[x][y] = count
            if max < count:
                max = count

        for i1 in range(n):
            for i2 in range(n):
                if max == arr[i1][i2]:
                    answer2.append((i1, i2))

        # 2번 조건을 만족하는 위치가 여러 개라면 3번 조건 체크
        if len(answer2) == 1:
            return answer2[0]
        else:
            answer2.sort(key=lambda x:x[0])
            x1, y1 = answer2[0]
            x2, y2 = answer2[1]
            if x1 != x2:
                return (x1, y1)
            else:
                if y1 < y2:
                    return (x1, y1)
                else:
                    (x2, y2)

def main():
    n = int(sys.stdin.readline())
    students = [['0'] for _ in range(n * n)]

    # 학생 n*n명의 순서와 각 학생이 좋아 하는 학생
    studentandlike = [[0] for _ in range(n*n + 1)]

    for i in range(n * n):
        students[i] = list(sys.stdin.readline().split())
        studentandlike[int(students[i][0])] = students[i][1:]

    # 자리
    seats = [['0'] * n for _ in range(n)]

    for student in students:
        # 학생과 학생이 좋아 하는 리스트
        s, likes = student[0], student[1:]

        # 조건 만족하는 자리
        start = []
        for i1 in range(n):
            for i2 in range(n):
                if seats[i1][i2] == '0':
                    start.append((i1, i2))

        x, y = bfs(seats, likes, n, start)
        seats[x][y] = s

    total = 0
    score = [0, 1, 10, 100, 1000]
    for i1 in range(n):
        for i2 in range(n):
            count = 0
            for i in range(4):
                nx, ny = i1 + dx[i], i2 + dy[i]
                if 0 <= nx < n and 0 <= ny < n and seats[nx][ny] in studentandlike[int(seats[i1][i2])]:
                    count += 1

            total += (score[count])
    print(total)

main()