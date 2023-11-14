def solution(babbling):
    answer = 0
    for b in babbling:
        for a in ["aya", "ye", "woo", "ma"]:
            if a*2 not in b:
                b = b.replace(a, " ")
        if len(b.strip()) == 0:
            answer += 1
    return answer