for test_case in range(1, int(input()) + 1):
    answer = {}
    score = []
    arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    n, student = map(int, input().split())

    for i in range(n):
        mid, fin, report = map(int, input().split())
        total = (mid*0.35 + fin*0.45 + report*0.2)
        answer[total] = i
        score.append(total)

    index = 0
    flag = 0
    for s in sorted(score, reverse=True):
        answer[s] = arr[index]
        flag += 1
        if flag == n//10:
            index += 1
            flag = 0

    print(f"#{test_case} {answer[score[student-1]]}")