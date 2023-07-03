def solution(N, stages):
    answer = {}
    sum = 0
    
    for i in range(1, N + 1):
        count = stages.count(i)
        if (len(stages) - sum) <= 0:
            answer[i] = 0
        else: answer[i] = count/(len(stages) - sum)
        sum += count
    
    answer = dict(sorted(answer.items(), key = lambda x:x[1], reverse = True))
    
    return [x for x in answer.keys()]