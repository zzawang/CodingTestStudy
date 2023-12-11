from collections import deque
def bfs(numbers, target):
    answer = 0
    q = deque([(numbers[0], 1), (-numbers[0], 1)])
    while q:
        s1, c1 = q.popleft()
        s2, c2 = q.popleft()
        if s1 == target and c1 == len(numbers):
            answer += 1
        if s2 == target and c2 == len(numbers):
            answer += 1
        if c1 < len(numbers):
            q.append((s1 + numbers[c1], c1 + 1))
            q.append((s1 - numbers[c1], c1 + 1))
        if c2 < len(numbers):
            q.append((s2 + numbers[c2], c2 + 1))
            q.append((s2 - numbers[c2], c2 + 1))
            
    return answer

def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer