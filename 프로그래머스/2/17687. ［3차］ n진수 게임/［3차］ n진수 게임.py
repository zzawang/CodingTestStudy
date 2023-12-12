def convert(num, n):
    result = ""
    alpha = "0123456789ABCDEF"
    if num == 0:
        return "0"
    else:
        while num >= 1:
            result = alpha[num % n] + result
            num //= n
            
    return result

def solution(n, t, m, p):
    result = ""
    for i in range(t * m + 1):
        result += convert(i, n)
        
    answer = ""
    index = p - 1
    while len(answer) < t:
        answer += result[index]
        index += m
        
    return answer