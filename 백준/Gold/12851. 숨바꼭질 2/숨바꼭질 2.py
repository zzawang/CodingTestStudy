import sys
from collections import deque

start, target = map(int, sys.stdin.readline().split())
queue = deque([start])
visited = [0] * 100001
count, answer = 0, 0

while queue:
    x = queue.popleft()
    temp = visited[x]
    if x == target:
        answer = temp
        count += 1
        continue

    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i < 100001:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i)
            elif visited[i] == visited[x] + 1:
                queue.append(i)

print(answer)
print(count)
