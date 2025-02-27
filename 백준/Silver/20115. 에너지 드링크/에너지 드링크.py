import sys

n = int(sys.stdin.readline())
drinks = sorted(list(map(int, sys.stdin.readline().split())))

print(round(sum(drinks[:n - 1]) / 2 + drinks[-1], 2))
