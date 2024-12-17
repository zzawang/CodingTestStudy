def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
        
    quot = s // n
    remain = s % n
    
    for num in range(n):
        answer.append(quot)
        
    if remain != 0:
        for index in range(n):
            answer[index] += 1
            remain -= 1
            if remain == 0:
                break

    return sorted(answer)