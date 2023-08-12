def solution(clothes):
    dic = {}
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 1
        else:
            dic[c[1]] += 1
    
    count = 1
    for d in dic.values():
        count *= (d + 1)  
    
    return count - 1  
