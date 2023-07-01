def solution(numbers):
    answer = []
    for i1 in range(len(numbers)):
        for i2 in range(len(numbers) - 1):
            if i1 == i2:
                continue
            if numbers[i1] + numbers[i2] not in answer:
                answer.append(numbers[i1] + numbers[i2])
                     
    return sorted(answer)