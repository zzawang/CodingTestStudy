import sys

n = 0
answer = float('inf')
cities = []
visited = []


def back_tracking(start, idx, total_sum, length):
    global n, answer, cities, visited

    if length == n:
        if cities[idx][start] > 0:
            total_sum += cities[idx][start]
            answer = min(answer, total_sum)
        return

    for i in range(n):
        if not visited[i] and cities[idx][i] > 0:
            visited[i] = True
            total_sum += cities[idx][i]
            back_tracking(start, i, total_sum, length + 1)
            visited[i] = False
            total_sum -= cities[idx][i]


def solution():
    global n, answer, cities, visited

    n = int(sys.stdin.readline())
    visited = [False] * n
    cities = []
    for _ in range(n):
        cities.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        visited[i] = True
        back_tracking(i, i, 0, 1)
        visited[i] = False

    print(answer)

solution()