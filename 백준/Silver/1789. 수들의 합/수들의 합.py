import sys

S = int(sys.stdin.readline().rstrip())
start = 1
end = S

while start <= end:
    mid = (start + end) // 2
    if mid * (mid + 1) // 2 <= S:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)