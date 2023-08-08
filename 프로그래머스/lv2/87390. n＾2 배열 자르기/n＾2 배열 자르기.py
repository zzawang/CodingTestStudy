def solution(n, left, right):
    tmp = [i+1 for i in range(n)]
    arr = []
    
    for i1 in range(left//n, right//n + 1):
        for i2 in range(i1):
            tmp[i2] = i1 + 1
        arr.extend(tmp)
    
    return arr[left%n: (right//n - left//n)*n + right%n + 1]