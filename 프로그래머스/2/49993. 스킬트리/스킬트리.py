def solution(skill, skill_trees):
    answer = 0
    
    for sts in skill_trees:
        stack = [s for s in skill]
        for st in sts:
            if stack and st in stack and st != stack[0]:
                break
            elif stack and st in stack and st == stack[0]:
                stack.pop(0)
        else:
            answer += 1
    
    return answer