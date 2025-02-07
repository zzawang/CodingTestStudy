n, m = 0, 0
answer = []
nums = []
visited = []

def bt(idx, length):
    global n, m, answer, nums, visited

    if length == m:
        print(*answer)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            answer.append(nums[i])
            bt(i, length + 1)
            visited[i] = False
            answer.pop()


def solution():
    global n, m, nums, visited
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    visited = [False] * (n + 1)
    bt(0, 0)

solution()