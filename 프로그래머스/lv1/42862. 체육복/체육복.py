def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lists = []
    
    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
    for l in lost:
        if l in reserve:
            lists.append(l)
            reserve.remove(l)
    for v in lists:
        if v in lost:
            lost.remove(v)

    answer = len(lost)
    if len(lost) > 0:
        for s in lost:
            if s-1 in reserve:
                answer -= 1
                reserve.remove(s-1)
            elif s+1 in reserve:
                answer -= 1
                reserve.remove(s+1)
        return n - answer
    else:
        return n
            