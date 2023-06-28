def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if sum(d[:i + 1]) > budget:
            return i
        if sum(d[:i + 1]) == budget or i == len(d) - 1:
            return i + 1