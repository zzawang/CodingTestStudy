import sys
import heapq

N = int(sys.stdin.readline().rstrip())  # 돌의 개수
A = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [float('inf')] * N
dp[0] = 0
min_heap = [(0, 0)]

while min_heap:
    cost, i = heapq.heappop(min_heap)

    if cost > dp[i]:
        continue

    for j in range(i + 1, N):
        power = (j - i) * (1 + abs(A[i] - A[j]))
        ncost = max(dp[i], power)

        if ncost < dp[j]:
            dp[j] = ncost
            heapq.heappush(min_heap, (ncost, j))

print(dp[N - 1])