import sys
k = 0
s = []
visited = []
answer = []

def bt(idx, length):
    global k, s, visited, answer

    if length == 6:
        print(*answer)
        return

    for i in range(idx, k):
        if not visited[i]:
            visited[i] = True
            answer.append(s[i])
            bt(i, length + 1)
            visited[i] = False
            answer.pop()

def solution():
    count = 0
    while True:
        count += 1
        global k, s, visited, answer
        arr = list(map(int, sys.stdin.readline().split()))

        if arr == [0]:
            break

        if count > 1:
            print()

        k, s = arr[0], arr[1:]
        visited = [False] * (k + 1)
        bt(0, 0)

solution()