N = int(input())
products = []
for _ in range(N):
    products.append(int(input()))
products.sort(reverse=True)

for i in range(N):
    if (i + 1) % 3 == 0:
        products[i] = 0

print(sum(products))