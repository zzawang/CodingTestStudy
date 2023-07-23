def solution(s):
    answer = ''
    pre = ''
    for v in s:
        new = v
        if v.isalpha():
            if pre == ' ' or pre == '':
                new = v.upper()
            else:
                new = v.lower()
                
        answer += new
        pre = new
            
    return answer