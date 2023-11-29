from collections import deque
def solution(priorities, location):
    answer = []
    q = deque(priorities)
    sequence = deque([x for x in range(len(priorities))])
    
    while q:
        p = q.popleft()
        s = sequence.popleft()

        if q and p < max(q):
            q.append(p)
            sequence.append(s)
        else:
            answer.append(s)

    return answer.index(location) + 1