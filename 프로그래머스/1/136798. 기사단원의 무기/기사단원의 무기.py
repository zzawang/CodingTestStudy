def yaksu(n):
    yaksu_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yaksu_list.append(i)
            yaksu_list.append(n // i)
    
    return len(set(yaksu_list))

def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        if yaksu(n) > limit:
            answer += power
        else:
            answer += yaksu(n)
        
    return answer