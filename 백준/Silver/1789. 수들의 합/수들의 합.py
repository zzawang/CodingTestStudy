import sys

def chk(n, S):
    return n * (n + 1) // 2 > S

S = int(sys.stdin.readline().rstrip())
left, right = 1, 93000

while left <= right:
    mid = (left + right) // 2
    if chk(mid, S):
        right = mid - 1
    else:
        left = mid + 1

print(right)
