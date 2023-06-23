def solution(price, money, count):
    answer = money - price * sum([i for i in range(1, count+1)])
    return -answer if answer < 0 else 0