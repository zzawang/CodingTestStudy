from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
dp = []

for num in nums:
    if not dp or dp[-1] < num:
        dp.append(num)
    else:
        index = bisect_left(dp, num)
        dp[index] = num

print(len(dp))
