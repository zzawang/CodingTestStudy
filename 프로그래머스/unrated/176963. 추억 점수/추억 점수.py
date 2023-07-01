def solution(name, yearning, photo):
    my_dict = {}
    for n, y in list(zip(name, yearning)):
        my_dict[n] = y
        
    answer = []
    
    for v1 in photo:
        sum = 0
        for v2 in v1:
            if v2 in my_dict.keys():
                sum += my_dict[v2]
        answer.append(sum)

    return answer