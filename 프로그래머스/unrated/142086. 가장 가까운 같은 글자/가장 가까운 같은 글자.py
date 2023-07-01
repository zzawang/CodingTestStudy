def solution(s):
    answer = []
    my_dict = {}
    
    for i, v in enumerate(s):
        if v not in my_dict.keys():
            answer.append(-1)
        else:
            answer.append(i - my_dict[v])
        my_dict[v] = i
            
    return answer