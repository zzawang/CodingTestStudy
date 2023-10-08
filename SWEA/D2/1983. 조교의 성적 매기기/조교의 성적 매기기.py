for test_case in range(1, int(input()) + 1):
    score = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    n, student = map(int, input().split())

    for i in range(n):
        mid, fin, report = map(int, input().split())
        total = (mid*0.35 + fin*0.45 + report*0.2)
        score.append(total)

    # 구하려는 학생의 총 점수
    find_score = score[student-1]

    score.sort(reverse=True)
    idx = score.index(find_score)
    answer = grade[idx//(n//10)]

    print(f"#{test_case} {answer}")