import sys

def binary_search(target):
    start, end = 0, target
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == target:
            return mid
        elif mid * mid >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

N = int(sys.stdin.readline().rstrip())
print(binary_search(N))