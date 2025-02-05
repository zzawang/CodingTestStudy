n = 0
m = 0
arr = []
visited = []

def solution():
    global n, m, arr, visited
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    arr = []
    back_tracking()

def back_tracking():
    global n, m, arr, visited
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            back_tracking()
            arr.pop()
            visited[i] = False

solution()