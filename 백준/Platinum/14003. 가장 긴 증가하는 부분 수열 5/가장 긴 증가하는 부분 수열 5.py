from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
lis = [nums[0]]
dp = [(0, nums[0])]

for i in range(1, n):
    if lis[-1] < nums[i]:
        lis.append(nums[i])
        dp.append((len(lis) - 1, nums[i]))
    else:
        index = bisect_left(lis, nums[i])
        lis[index] = nums[i]
        dp.append((index, nums[i]))

max_length = len(lis)
print(max_length)

last_index = max_length - 1
answer = []
for i in range(len(dp) - 1, -1, -1):
    index, num = dp[i]
    if last_index == index:
        answer.append(num)
        last_index -= 1

print(*answer[::-1])