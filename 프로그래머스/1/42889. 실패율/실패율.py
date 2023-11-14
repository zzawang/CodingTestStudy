def solution(N, stages):
    answer = {}
    sum = 0
    
    for i in range(1, N + 1):
        stage_count = stages.count(i)
        if (len(stages) - sum) <= 0:
            answer[i] = 0
        else:
            answer[i] = stage_count/(len(stages) - sum)
        sum += stage_count
        
    return sorted(answer, key = lambda x:-answer[x])