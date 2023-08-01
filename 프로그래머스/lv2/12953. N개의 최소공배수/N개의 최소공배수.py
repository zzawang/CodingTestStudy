import math
def solution(arr):
    answer = arr[0] if len(arr) == 1 else (arr[0]*arr[1]) // math.gcd(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = (answer*arr[i]) // math.gcd(answer, arr[i])
        
    return answer