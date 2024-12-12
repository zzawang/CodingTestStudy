import heapq

def solution(operations):
    answer = []
    for operation in operations:
        command, str_num = operation.split()
        num = int(str_num)
        if command == 'I':
            heapq.heappush(answer, num)
        elif command == 'D' and len(answer) != 0:
            if num == 1:
                answer = heapq.nlargest(len(answer), answer)[1:]
            elif num == -1:
                heapq.heappop(answer)
        heapq.heapify(answer)
        
    if len(answer) == 0:
        return [0, 0]
    
    return [max(answer), min(answer)]