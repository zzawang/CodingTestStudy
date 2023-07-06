def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        i = str(i)
        for _ in range(min(X.count(i), Y.count(i))):
            answer += i
        
    if answer == '':
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer
    