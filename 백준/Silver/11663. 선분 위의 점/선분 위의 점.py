import sys

def find_start(s):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        if point[mid] < s:
            start = mid + 1
        else:
            end = mid - 1

    return start

def find_end(e):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2
        if point[mid] <= e:
            start = mid + 1
        else:
            end = mid - 1

    return start

N, M = map(int, sys.stdin.readline().rstrip().split())
point = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    print(find_end(e) - find_start(s))