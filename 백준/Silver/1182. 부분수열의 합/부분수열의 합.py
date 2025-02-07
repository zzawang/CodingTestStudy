import sys

n, s = 0, 0
nums = []  # 수열
arr = []  # 부분 수열
count = 0  # 원소를 다 더한 값이 S인 부분 수열의 개수

def bt(idx):
    global n, s, nums, arr, count

    if len(arr) >= n:
        if sum(arr) == s:
            count += 1
        return
    else:
        if arr and sum(arr) == s:
            count += 1
        for i in range(idx, n):
            arr.append(nums[i])
            bt(i + 1)
            arr.pop()

def solution():
    global n, s, nums, count
    n, s = map(int, sys.stdin.readline().split())
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    bt(0)
    print(count)

solution()