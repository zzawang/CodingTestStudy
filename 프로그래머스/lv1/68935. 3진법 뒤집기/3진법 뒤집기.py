def tenTothree(num):
    result = ''
    
    while num > 0:
        remain = num % 3
        result = str(remain) + result
        num = num//3
        
    return result
        
def solution(n):
    return int(tenTothree(n)[::-1], 3)