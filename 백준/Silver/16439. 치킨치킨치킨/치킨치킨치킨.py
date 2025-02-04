from itertools import combinations

n, m = map(int, input().split())
arr = [n for n in range(m)]
want = []
for _ in range(n):
    want.append(list(map(int, input().split())))

answer = 0
for a, b, c in list(combinations(arr, 3)):
    love = 0
    for member in range(n):
        love += max(want[member][a], want[member][b], want[member][c])

    answer = max(answer, love)

print(answer)