n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
count = 0
answer = 100000

while end < n:
    count += nums[end]
    end += 1

    while count - nums[start] >= s and start < end:
        count -= nums[start]
        start += 1

    if count >= s:
        answer = min(answer, end - start)

if answer == 100000:
    print(0)
else:
    print(answer)