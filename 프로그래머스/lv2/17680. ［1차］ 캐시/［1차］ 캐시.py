def solution(cacheSize, cities):
    stack = []
    answer = 0
    for c in cities:
        c = c.lower()
        if len(stack) < cacheSize and c not in stack:
            answer += 5
            stack.append(c)
        elif c in stack:
            answer += 1
            index = stack.index(c)
            stack = stack[:index] + stack[index + 1:]
            stack.append(c)
        elif c not in stack:
            answer += 5
            if cacheSize > 0:
                stack = stack[1:cacheSize]
                stack.append(c)
    return answer