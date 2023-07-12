def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, p in enumerate(participant):
        if i >= len(completion) or p != completion[i]:
            return p