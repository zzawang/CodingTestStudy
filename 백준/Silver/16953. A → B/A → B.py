import sys
from collections import deque

def find_num(a, b):
    q = deque([(a, 1)])

    while q:
        n, count = q.popleft()
        if n == b:
            return count
        elif n < b:
            q.append((int(str(n) + "1"), count + 1))
            q.append((n * 2, count + 1))

    return -1

a, b = map(int, sys.stdin.readline().split())
print(find_num(a, b))
