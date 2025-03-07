import sys

def find_pivot(end):
    start = 1

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for line in lines:
            count += line // mid

        if count >= N:
            start = mid + 1
        elif count < N:
            end = mid - 1

    return end

K, N = map(int, sys.stdin.readline().rstrip().split())

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline().rstrip()))

print(find_pivot(max(lines)))
