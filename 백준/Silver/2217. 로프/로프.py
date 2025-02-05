answer = -1
n = int(input())
lopes = []
for _ in range(n):
    lopes.append(int(input()))

lopes.sort(reverse=True)

for i, lope in enumerate(lopes):
    answer = max(answer, lopes[i] * (i + 1))

print(answer)