n, m = 0, 0
answer = []
nums = []

def bt(idx, length):
    global n, m, answer, nums

    if length == m:
        print(*answer)
        return

    for i in range(idx, n):
        answer.append(nums[i])
        bt(i, length + 1)
        answer.pop()


def solution():
    global n, m, nums
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    bt(0, 0)

solution()