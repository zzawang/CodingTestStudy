def solution(citations):
    for i, c in enumerate(sorted(citations)):
        if c > len(citations) - i:
            return len(citations) - i
    return 0