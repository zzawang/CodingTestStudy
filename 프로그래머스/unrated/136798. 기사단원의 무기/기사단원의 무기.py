import math
def solution(number, limit, power):
    answer = []
    for i in range(1, number+1):
        answer.append(yaksu(i, limit, power))
    
    return sum(answer)

def yaksu(n, limit, power):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            sum += 1
            if i != n // i:  
                sum += 1
            
    return sum if sum <= limit else power