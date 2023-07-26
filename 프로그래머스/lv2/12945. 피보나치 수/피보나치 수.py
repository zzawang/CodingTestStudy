def solution(n):
    fibo = {}
    fibo[0], fibo[1] = 0, 1
    for i in range(2, n + 1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]%1234567