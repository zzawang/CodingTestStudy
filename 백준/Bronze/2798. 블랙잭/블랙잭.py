n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = []

for i1 in range(n):
    for i2 in range(n):
        if i1 == i2:
            continue
        for i3 in range(n):
            if i1 == i3 or i2 == i3:
                continue
            if cards[i1] + cards[i2] + cards[i3] <= m:
                answer.append(cards[i1] + cards[i2] + cards[i3])

print(max(answer))