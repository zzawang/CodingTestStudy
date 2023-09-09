import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
length = len(arr)
sum = 0
for a in arr:
    sum += (a*length)
    length -= 1

print(sum)