from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    cards.append(input())

answer = set()
for card in list(permutations(cards, k)):
    answer.add(int("".join(card)))

print(len(answer))