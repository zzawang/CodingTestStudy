n = 0
m = 0
answer = []
visited = []

def bt(num):
    global n, m, answer, visited
    if len(answer) == m:
        print(*answer)
        return

    for i in range(num, n + 1):
        if not visited[i]:
            if len(answer) == 0 or (len(answer) > 0 and answer[-1] < i):
                visited[i] = True
                answer.append(i)
                bt(num)
                visited[i] = False
                answer.pop()

def solution():
    global n, m, visited
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    bt(1)

solution()