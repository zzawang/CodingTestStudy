def solution(players, callings):
    dic1 = {}
    dic2 = {}
    for i, p in enumerate(players):
        dic1[p] = i
        dic2[i] = p
        
    for c in callings:
        index = dic1[c]
        pre = dic2[index - 1]
        dic1[c] -= 1
        dic1[pre] += 1
        dic2[index - 1], dic2[index] = dic2[index], dic2[index - 1]
        
    return [x for x in dic2.values()]