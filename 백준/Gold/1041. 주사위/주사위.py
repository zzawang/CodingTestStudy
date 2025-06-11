import sys
import heapq

n = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(sum(heapq.nsmallest(5, f)))
else:
    m = sorted([min(f[0], f[5]), min(f[1], f[4]), min(f[2], f[3])])
    print(
        (n-2)**2 * min(f) + 4*(n-1)*(n-2)*min(f) +
        (4*(n-2)+4*(n-1)) * sum(m[:2]) + 4 * sum(m)
    )
