import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

answer = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    answer += (a+b)
    heapq.heappush(heap, a+b)
print(answer)
