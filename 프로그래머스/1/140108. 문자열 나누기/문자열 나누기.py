def solution(s):
    x = s[0]
    isx = 0
    notx = 0
    answer = 0
    
    for ss in s:
        if isx == notx:
            x = ss
            isx = 0
            notx = 0
            answer += 1
            
        if ss == x:
            isx += 1
        else:
            notx += 1
    
    return answer