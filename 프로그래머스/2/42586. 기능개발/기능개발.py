import math
def solution(progresses, speeds):
    answer = []
    time = []
    for i, p in enumerate(progresses):
        t = math.ceil((100 - p) / speeds[i])
        time.append(t)
        
    max = 0
    count = 0
    for i in range(len(time)):
        if time[i] <= max:
            count += 1
        else:
            if count != 0:
                answer.append(count)
            max = time[i]
            count = 1
            
    answer.append(count)
    
    return answer