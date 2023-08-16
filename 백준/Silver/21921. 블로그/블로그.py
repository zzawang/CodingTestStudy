import sys

N, X = map(int, sys.stdin.readline().split(" "))
visiters = list(map(int, sys.stdin.readline().split(" ")))

# Sliding Window

windowSum = 0
maxCount = 1
max = 0

for i, value in enumerate(visiters):
    windowSum += value
    if i >= X - 1:
        if windowSum > max:
            max = windowSum
            maxCount = 0
        if windowSum == max & max != 0:
            maxCount += 1
        windowSum -= visiters[i - X + 1]

if max == 0:
    print("SAD")
else:
    print(max)
    print(maxCount)