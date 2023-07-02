def solution(answers):
    answer = []
    
    a_count = 0
    b_count = 0
    c_count = 0
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, v in enumerate(answers):
        if v == a[i%len(a)]:
            a_count += 1
        if v == b[i%len(b)]:
            b_count += 1
        if v == c[i%len(c)]:
            c_count += 1
            
    m = max(a_count, b_count, c_count)
    if a_count == m:
        answer.append(1)
    if b_count == m:
        answer.append(2)
    if c_count == m:
        answer.append(3)
            
    return answer