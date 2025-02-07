import sys

n, m = 0, 0
nums = []  # 수열
arr = [] # N개의 자연수 중에서 M개를 고른 수열
visited = [] # 수 방문 여부

def dfs(length):
    global n, m, nums, arr, visited

    if length == m:
        print(*arr)
        return

    prev = 0
    for i in range(n):
        if not visited[i] and prev != nums[i]:
            visited[i] = True
            arr.append(nums[i])
            prev = nums[i]
            dfs(length + 1)
            arr.pop()
            visited[i] = False

def solution():
    global n, m, nums, visited
    n, m = map(int, sys.stdin.readline().split())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    visited = [False] * n
    dfs(0)

solution()