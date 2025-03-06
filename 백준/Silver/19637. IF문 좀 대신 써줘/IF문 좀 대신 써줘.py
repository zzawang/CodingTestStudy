import sys

def binary_search(target):
    N = len(title)
    start, end = 0, N - 1
    result = 0

    while start <= end:
        mid = (start + end) // 2
        mt, mp = title[mid]
        if target <= mp:
            result = mt
            end = mid - 1
        else:
            start = mid + 1
    return result

N, M = map(int, sys.stdin.readline().rstrip().split())
title = []
for _ in range(N):
    t, p = sys.stdin.readline().rstrip().split()
    title.append((t, int(p)))

for i in range(M):
    power = int(sys.stdin.readline().rstrip())
    print(binary_search(power))