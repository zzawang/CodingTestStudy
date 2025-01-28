n = int(input())
answer = []

for i in range(n - 1, 0, -1):
    result = i + sum([int(s) for s in str(i)])
    if result == n:
        answer.append(i)

if len(answer) == 0:
    print(0)
else:
    print(min(answer))