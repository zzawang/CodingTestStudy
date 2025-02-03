from itertools import permutations
def isSosu(num):
    if num <= 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    result = set([int(n) for n in numbers])
    for i in range(2, len(nums) + 1):
        for n in list(permutations(nums, i)):
            result.add(int("".join(n)))
        
    for num in result:
        if isSosu(num):
            answer += 1
    
    return answer