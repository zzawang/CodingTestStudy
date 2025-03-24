import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

start, end = 1, arr[-1] - arr[0]  # 최소 공유기 거리, 최대 공유기 거리
answer = 0

# 두 공유기 사이의 거리 찾기
while start <= end:
    mid = (start + end) // 2  # 현재 공유기 거리
    current = arr[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        answer = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(end)