n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i): # i 이전의 수 중 최대 찾기
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)
print(max_length)

answer = []
for i in range(n - 1, -1, -1): # 가장 긴 증가하는 부분 수열 찾기
    if dp[i] == max_length:
        answer.append(nums[i])
        max_length -= 1

print(*sorted(answer))