def solution(a, b, n):
    # n = 현재 가지고 있는 병의 개수
    remain = 0 # a개 미만이라 가지고 있는 빈 병의 개수
    answer = 0 # 받은 콜라 개수
    
    while n > 0:
        if remain > 0:
            n += remain
            remain = 0
        answer += (n//a)*b
        remain += n%a  
        n = (n//a)*b  
    
    return answer