from itertools import combinations

def solution(nums):
    num = list(combinations(nums, 3))
    return sum(yaksu(sum(v)) for v in num)

def yaksu(n):
    boolean = False
    
    for y in range(2, n//2):
        if n % y == 0:
            boolean = True
    
    return 1 if boolean == False else 0