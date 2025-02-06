n, k = map(int, input().split())
temps = list(map(int, input().split()))

result = sum(temps[:k])
answer = [result]

for i in range(n - k):
    result += (temps[i + k] - temps[i])
    answer.append(result)

print(max(answer))
