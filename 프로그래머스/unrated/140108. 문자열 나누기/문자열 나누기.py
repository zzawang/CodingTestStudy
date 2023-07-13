def solution(s):
    index1 = 0
    index2 = 0
    first = s[0]
    answer = 0
    count = 0
    
    for i, v in enumerate(s):
        if v == first:
            index1 += 1
        else:
            index2 += 1
            
        if index1 == index2:
            answer += 1
            if i < len(s)-1:
                first = s[i + 1]
            count = count + index1 + index2
            index1 = 0
            index2 = 0
            
    if count != len(s):
        answer += 1

    return answer