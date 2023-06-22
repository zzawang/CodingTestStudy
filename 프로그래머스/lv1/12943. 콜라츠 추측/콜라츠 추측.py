def solution(num):
    if num == 1:
        return 0
    
    count = 0
    while num != 1:
        if num % 2 == 0:  # 짝수인 경우
            num = num // 2
        else:  # 홀수인 경우
            num = num * 3 + 1

        count += 1

        if count == 500:  # 500번 반복하였을 때
            return -1

    return count
