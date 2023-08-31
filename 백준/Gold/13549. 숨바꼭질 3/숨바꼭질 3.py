from collections import deque
n, k = map(int, input().split())
visited = [False] * (100001)
q = deque([(0, n)])

while q:
    day, s = q.popleft()
    if s == k:
        print(day)
        break
    for num in (s*2, s-1, s+1):
        if 0 <= num < 100001 and not visited[num]:
            visited[num] = True
            if num == s*2:
                q.append((day, num))
            else:
                q.append((day + 1, num))