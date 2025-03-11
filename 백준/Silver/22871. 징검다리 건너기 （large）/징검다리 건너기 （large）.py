import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, arr):
    dp = [float('inf')] * n
    dp[0] = 0
    min_heap = [(0,0)]

    while min_heap:
        cost, i = heapq.heappop(min_heap)

        if cost > dp[i]:
            continue

        for j in range(i+1, n):
            cost2 = (j-i) * (1 + abs(arr[i] - arr[j]))
            ncost = max(dp[i], cost2)

            if ncost < dp[j]:
                dp[j] = ncost
                heapq.heappush(min_heap, (ncost, j))

    return dp[n-1]


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))