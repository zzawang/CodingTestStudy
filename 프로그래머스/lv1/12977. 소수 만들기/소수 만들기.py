def solution(nums):
    num = []
    
    for i1 in range(len(nums) - 2):
        for i2 in range(i1 + 1, len(nums) - 1):
            for i3 in range(i2 + 1, len(nums)):
                num.append(nums[i1] + nums[i2] + nums[i3])
    
    return sum(yaksu(v) for v in num)

def yaksu(n):
    boolean = False
    
    for y in range(2, n//2):
        if n % y == 0:
            boolean = True
    
    return 1 if boolean == False else 0