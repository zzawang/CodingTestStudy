n = int(input())
nums = sorted(list(map(int, input().split())))
answer = 0

for i in range(n):
    temp = nums[:i] + nums[i + 1:]
    start, end = 0, len(temp) - 1
    while start < end:
        total = temp[start] + temp[end]
        if total == nums[i]:
            answer += 1
            break
        elif total < nums[i]:
            start += 1
        else:
            end -= 1

print(answer)