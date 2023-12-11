def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True
    
def solution(n, k):
    answer = 0
    number = ""
    while n >= 1: # k진수 구하기
        number = str(n % k) + number
        n //= k
        
    for num in number.split("0"):
        if num and isPrime(int(num)):
            answer += 1
        
    return answer