def solution(n, m, section):
    answer = 1
    paint = section[0] + m - 1
    for s in section:
        if s > paint:
            paint = s + m - 1
            answer += 1
    return answer