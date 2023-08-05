def solution(elements):
    answer = []
    for i1 in range(1, len(elements) + 1):
        for i2 in range(0, len(elements)):
            if i2 == len(elements):
                answer.append(elements[i2] + sum(elements[0:(i1 + i2)%len(elements)]))
            elif  i1 + i2 >= len(elements):
                answer.append(sum(elements[i2:]) + sum(elements[0:(i1 + i2)%len(elements)]))
            else:
                answer.append(sum(elements[i2:i1 + i2]))
    
    return len(set(answer))