def solution(dartResult):
    answer = []
    area = {"S" : 1, "D" : 2, "T" : 3}
    string = ""
    flag = False
    
    for v in dartResult:
        string += v
        if v.isdigit():
            flag = True
        if not v.isdigit() and flag:
            answer.append(string)
            string = ""

    for i, a in enumerate(answer):
        if a == '*':
            answer[i - 1] *= 2
            answer[i] = 0
            if i - 2 >= 0:
                if answer[i - 2] == 0:
                    answer[i - 3] *= 2
                else:
                    answer[i - 2] *= 2
        elif a == '#':
            answer[i - 1] = -answer[i - 1]
            answer[i] = 0
        else:
            operator = len(a) - 1
            answer[i] = int(a[0:operator]) ** area[a[operator]]

    return sum(answer)