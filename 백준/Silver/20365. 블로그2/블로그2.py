import sys

n = int(sys.stdin.readline())
colors = list(c for c in sys.stdin.readline().rstrip())
counter = {'B': 0, 'R': 0}

start = colors[0]
for i in range(1, n):
    end = colors[i]
    if start != end:
        counter[start] += 1
        start = end

counter[start] += 1
print(min(counter['B'], counter['R']) + 1) # 최소 구간 값 + 1
