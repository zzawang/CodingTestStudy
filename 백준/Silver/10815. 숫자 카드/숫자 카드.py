import sys

N = int(sys.stdin.readline().rstrip())
answer = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

find = {}
for a in answer:
    find[a] = True

result = []
for c in cards:
    if find.get(c) is not None:
        result.append(1)
    else:
        result.append(0)

print(*result)