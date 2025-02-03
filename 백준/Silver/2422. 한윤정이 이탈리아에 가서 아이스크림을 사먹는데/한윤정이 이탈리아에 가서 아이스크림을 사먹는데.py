from collections import defaultdict
n, m = map(int, input().split())

combination = []
for i1 in range(1, n + 1):
    for i2 in range(i1 + 1, n + 1):
        for i3 in range(i2 + 1, n + 1):
            combination.append((i1, i2, i3))

hate_combination = defaultdict(list)
for i in range(m):
    icecream1, icecream2 = map(int, input().split())
    hate_combination[icecream1].append(icecream2)

hates = 0
for comb in combination:
    a, b, c = comb
    if b in hate_combination[a] or c in hate_combination[a]:
        hates += 1
    elif a in hate_combination[b] or c in hate_combination[b]:
        hates += 1
    elif a in hate_combination[c] or b in hate_combination[c]:
        hates += 1

print(len(combination) - hates)