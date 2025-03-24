import sys
import heapq

N = int(sys.stdin.readline().rstrip())
events = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(events, (s, 's'))  # 시작 이벤트
    heapq.heappush(events, (e, 'e'))  # 종료 이벤트

answer = 0
rooms = 0

while events:
    time, event_type = heapq.heappop(events)

    if event_type == 's':  # 회의 시작
        rooms += 1
    else:  # 회의 종료
        rooms -= 1

    answer = max(answer, rooms)  # 최대 회의실 개수 갱신

print(answer)
