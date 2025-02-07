import sys

n = 0
nums = []
sign = []
expression = []
answer = []
visited = []

def dfs(length):
    global n, nums, s, answer, visited, sign, expression

    if length == n - 1:
        tmp = nums[0]
        for s in range(n - 1):
            if expression[s] == 0:
                tmp += nums[s + 1]
            elif expression[s] == 1:
                tmp -= nums[s + 1]
            elif expression[s] == 2:
                tmp *= nums[s + 1]
            else:
                if tmp < 0 < nums[s + 1]:
                    tmp = -(-tmp // nums[s + 1])
                else:
                    tmp //= nums[s + 1]

        answer.append(tmp)
        return

    for i in range(n - 1):
        if not visited[i]:
            visited[i] = True
            expression.append(sign[i])
            dfs(length + 1)
            expression.pop()
            visited[i] = False


def solution():
    global n, nums, s, answer, visited, sign

    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    arr = list(map(int, sys.stdin.readline().split()))
    sign = []
    for i, v in enumerate(arr):
        sign.extend([i] * v)

    visited = [False] * (n - 1)
    dfs(0)
    print(max(answer))
    print(min(answer))

solution()