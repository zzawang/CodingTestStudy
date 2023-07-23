def solution(s):
    answer = True
    stack = []
    
    # 스택에는 ( 만 집어넣기
    for s1 in s:
        if not stack and s1 == ')':
            answer = False
            break
        if stack and s1 == ')':
            stack.pop()
        else:
            if s1 == '(':
                stack.append(s1)
            else:
                answer = False
                break
    if stack:
        answer = False
    return answer