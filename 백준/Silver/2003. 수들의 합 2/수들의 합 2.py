n, m = map(int , input().split())
nums = list(map(int, input().split()))

left = 0
right = 1
answer = 0

while n >= right >= left:
    result = sum(nums[left:right])
    if result == m:
        answer += 1
        right += 1
    elif result < m:
        right += 1
    elif result > m:
        left += 1

print(answer)