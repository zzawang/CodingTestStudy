def solution(k, score):
    answer = []
    crown = []
    
    for v in score:
        if len(crown) < k:
            crown.append(v)
        else:
            if crown[crown.index(min(crown))] < v:
                crown[crown.index(min(crown))] = v
        answer.append(min(crown))
        
    return answer