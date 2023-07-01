def solution(k, m, score):
    score.sort(reverse = True)
    return sum(min(score[i*m:i*m+m])*m for i in range(len(score) // m))