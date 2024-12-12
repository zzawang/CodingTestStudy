import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)
    
    while n > 0:
        n -= 1
        work = -heapq.heappop(works)
        work -= 1
        heapq.heappush(works, -work)
    
    answer = 0
    for work in works:
        answer += work * work
    
    return answer