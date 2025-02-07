import sys

n = 0
nums = []
sign = []
answer = []

def dfs(length, temp):
    global n, nums, sign, answer

    if length == n - 1:
        answer.append(temp)
        return

    # 하부함수 호출
    if sign[0] > 0:
        sign[0] -= 1
        dfs(length + 1, temp + nums[length + 1])
        sign[0] += 1

    if sign[1] > 0:
        sign[1] -= 1
        dfs(length + 1, temp - nums[length + 1])
        sign[1] += 1

    if sign[2] > 0:
        sign[2] -= 1
        dfs(length + 1, temp * nums[length + 1])
        sign[2] += 1

    if sign[3] > 0:
        sign[3] -= 1
        dfs(length + 1, int(temp / nums[length + 1]))
        sign[3] += 1

def solution():
    global n, nums, sign, answer

    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    sign = list(map(int, sys.stdin.readline().split()))

    dfs(0, nums[0])
    print(max(answer))
    print(min(answer))

solution()