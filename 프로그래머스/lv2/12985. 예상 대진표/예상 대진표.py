def solution(n,a,b):
    for i in range(1, n//2 + 1):
        if min(a,b)%2 == 1 and abs(a-b) == 1:
            return i
        else:
            a = a//2 if a%2 == 0 else (a+1)//2
            b = b//2 if b%2 == 0 else (b+1)//2