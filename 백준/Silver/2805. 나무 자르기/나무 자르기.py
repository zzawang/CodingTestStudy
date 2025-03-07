import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
tree = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for t in tree:
        tmp = t - mid
        if tmp > 0:
            result += tmp

    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
