from collections import deque
n, k = map(int, input().split())
k_nums = list(map(int, input().split()))

answer = []
power = len(str(n)) # 자릿수에 사용되는 숫자
q = deque([])
for k_num in k_nums:
    q.append((10 ** (power - 1) * k_num, power - 1))

while q:
    num, pow = q.popleft()
    if pow == 0:
        answer.append(num)
    else:
        for k_num in k_nums:
            q.append((10 ** (pow - 1) * k_num, pow - 1))
            result = num + 10 ** (pow - 1) * k_num
            if result <= n:
                q.append((result, pow - 1))

print(max(answer))