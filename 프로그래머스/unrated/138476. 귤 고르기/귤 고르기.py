def solution(k, tangerine):
    count = 0
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    dic = dict(sorted(dic.items(), reverse = True, key=lambda x:x[1]))
    
    for x in dic:
        count += dic[x]
        answer += 1
        if count >= k:
            break
        
    return answer