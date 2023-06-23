def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        if yaksu(i)%2 ==0:
            sum += i
        else:
            sum -= i
    return sum

def yaksu(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1
    return count