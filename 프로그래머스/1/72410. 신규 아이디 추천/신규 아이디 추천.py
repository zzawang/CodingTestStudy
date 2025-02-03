def solution(new_id):
    giho = ['-', '_', '.']
    old_id = new_id.lower()
    new_id = ''
    for i1 in old_id:
        if i1 not in giho and not i1.isalpha() and not i1.isdigit():
            continue
        new_id += i1
    
    answer = ''
    for i, i2 in enumerate(new_id):
        if answer and answer[-1] == '.' and i2 == '.':
            continue
        answer += i2
        
    f = 1
    while answer[0] == '.':
        if answer == '':
            break
        if len(answer) == 1:
            answer = ''
            break
        answer = answer[f:]
        f += 1

    m = len(answer) - 1
    while answer and answer[-1] == '.':
        if answer == '':
            break
        if len(answer) == 1:
            answer = ''
            break
        answer = answer[:m]
        m -= 1
        
    if answer == '':
        answer = "a"
        
    if len(answer) >= 16:
        answer = answer[:15]
        
    m = len(answer) - 1
    while answer and answer[-1] == '.':
        if answer == '':
            break
        if len(answer) == 1:
            answer = ''
            break
        answer = answer[:m]
        m -= 1
        
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
            
    return answer