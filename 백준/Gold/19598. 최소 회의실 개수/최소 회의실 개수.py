import sys
import heapq

N = int(sys.stdin.readline().rstrip())
times = []

for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().rstrip().split())))

times.sort(key=lambda x:x[0])  # 시작시간을 기준으로 정렬

arr = [0]  # 최소 힙을 사용하기 위해 0으로 초기화
count = 1

for start, end in times:
    if start >= arr[0]: # 진행 중인 강의 종료시간보다 시작시간이 늦거나 같다면 강의 가능
        heapq.heappop(arr)
    else:
        count += 1
        
    heapq.heappush(arr, end)
print(count)