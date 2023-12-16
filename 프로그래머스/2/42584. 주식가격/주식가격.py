def solution(prices):
    answer = [ i for i in range(len(prices) - 1, -1, -1)]
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            p = stack.pop()
            answer[p] = i - p
            
        stack.append(i)
            
    return answer