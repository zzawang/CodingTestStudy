def solution(s):
    answer = 0
    dic = {'[' : ']', '(' : ')', '{' : '}'}
    for i in range(len(s)):
        str = s[i:] + s[0:i]
        
        check = []
        for st in str:
            if check and check[-1] in dic.keys():
                if dic[check[-1]] == st:
                    check.pop()
                else:
                    check.append(st)
            else:
                check.append(st)
        if check == []:
            answer += 1
        
    return answer