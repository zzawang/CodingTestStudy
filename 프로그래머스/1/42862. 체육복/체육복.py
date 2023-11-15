def solution(n, lost, reserve):
    answer = 0
    for l in sorted(lost):
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
            
    for l in sorted(lost):
        if l - 1 in reserve:
            lost.remove(l)
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            lost.remove(l)
            reserve.remove(l + 1)
            
    return n - len(lost)