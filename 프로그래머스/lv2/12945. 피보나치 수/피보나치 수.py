def solution(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, (a+b)%1234567
    return a