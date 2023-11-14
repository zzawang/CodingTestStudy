def solution(d, budget):
    answer = 0
    index = 0
    d.sort()
    for b in d:
        if sum(d[0:index + 1]) <= budget:
            answer += 1
        index += 1
    return answer