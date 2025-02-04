import sys
from itertools import combinations
from collections import Counter

t = input()
n = int(input())
books = []
for _ in range(n):
    price, book = input().split()
    books.append((int(price), book))

books.sort(key=lambda x:x[0]) # 가격 오름차순으로 정렬

answer = sys.maxsize
for i in range(1, n + 1):
    for comb in list(combinations(books, i)):
        flag = True
        total_price = 0
        total_name = ''
        for price, name in comb:
            total_price += price
            total_name += name

        words = dict(Counter(total_name))
        for word in t:
            if words.get(word) is None or words[word] == 0:
                flag = False
            else:
                words[word] -= 1

        if not flag:
            continue

        answer = min(answer, total_price)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
