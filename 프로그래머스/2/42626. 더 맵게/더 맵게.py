import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap[0] < K:
        answer += 1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        
        if len(heap) == 1 and heap[0] < K:
            return -1
    
    return answer