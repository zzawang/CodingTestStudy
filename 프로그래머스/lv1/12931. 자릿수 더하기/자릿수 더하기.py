def solution(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    
    return sum