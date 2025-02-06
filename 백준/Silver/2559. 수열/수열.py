n, k = map(int, input().split())
temps = list(map(int, input().split()))

left = 0
right = k - 1
result = sum(temps[left:right + 1])
answer = result

while right < n - 1:
    right += 1
    result += (temps[right] - temps[left])
    left += 1
    answer = max(answer, result)


print(answer)
