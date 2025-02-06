from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
n_dict = defaultdict(int)
answer = 0

while end < n:
    if n_dict[nums[end]] >= k:
        n_dict[nums[start]] -= 1
        start += 1
    else:
        n_dict[nums[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(answer)