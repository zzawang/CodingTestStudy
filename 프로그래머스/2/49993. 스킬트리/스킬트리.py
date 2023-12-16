def solution(skill, skill_trees):
    answer = 0
    
    for sts in skill_trees:
        stack = [s for s in skill][::-1]
        flag = True
        for st in sts:
            if stack and st in stack and st != stack[-1]:
                flag = False
                break
            elif stack and st in stack and st == stack[-1]:
                stack.pop()
        
        if flag:
            answer += 1
    
    return answer