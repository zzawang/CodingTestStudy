from itertools import permutations
def solution(k, dungeons):
    answer = -1
    results = list(permutations(dungeons, len(dungeons)))
    for result in results:
        sum = 0
        nk = k
        for a, b in result:
            if nk >= a:
                nk -= b
                sum += 1
            else:
                break
        answer = max(answer, sum)
    return answer