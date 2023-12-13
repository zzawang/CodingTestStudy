def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            index = stack.pop()
            answer[index] = num
        stack.append(i)
        
    return answer