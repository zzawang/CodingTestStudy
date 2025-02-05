n = int(input())
customers = []
for _ in range(n):
    customers.append(int(input()))
customers.sort(reverse=True)

answer = 0
for i, customer in enumerate(customers):
    result = customer - i
    if result > 0:
        answer += result

print(answer)