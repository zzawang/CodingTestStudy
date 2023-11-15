def solution(participant, completion):
    answer = ''
    index = 0
    answer_list = []
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            answer_list.append(p)
            answer_list.append(c)
            break
        index += 1
            
    if answer_list != []:
        for an in answer_list:
            if an != participant[index + 1]:
                answer = an
    else:
        answer = participant[len(participant) - 1]
    return answer