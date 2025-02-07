import sys

n, m = 0, 0
nums = []  # 수열
arr = [] # N개의 자연수 중에서 M개를 고른 수열

def dfs(idx, length):
    global n, m, nums, arr

    if length == m:
        print(*arr)
        return

    prev = 0
    for i in range(n):
        if prev != nums[i]:
            prev = nums[i]
            arr.append(nums[i])
            dfs(i, length + 1)
            arr.pop()

def solution():
    global n, m, nums
    n, m = map(int, sys.stdin.readline().split())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    dfs(0, 0)

solution()