def solution(survey, choices):
    answer = ''
    dic = {
        'A' : 0, 'N' : 0,
        'C' : 0, 'F' : 0,
        'M' : 0, 'J' : 0,
        'R' : 0, 'T' : 0,
    }
    
    for i, c in enumerate(choices):
        if c == 4:
            continue
        if c < 4:
            dic[survey[i][0]] = dic[survey[i][0]] + 4 - c
        else:
            dic[survey[i][1]] = dic[survey[i][1]] + c - 4
            
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer