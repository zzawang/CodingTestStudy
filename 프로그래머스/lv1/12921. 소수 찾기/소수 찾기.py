import math

def solution(n):
    array = [True]*(n + 1) # 처음엔 모두가 다 소수
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            j = 2
            while i * j <= n :
                array[i * j] = False
                j += 1
        
    return array[2:].count(True)