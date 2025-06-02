n = int(input())
a, b, c = map(int, input().split())
prev = [[a, a], [b, b], [c, c]]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    curr = [[0, 0] for _ in range(3)]

    curr[0][0] = a + min(prev[0][0], prev[1][0])
    curr[0][1] = a + max(prev[0][1], prev[1][1])

    curr[1][0] = b + min(prev[0][0], prev[1][0], prev[2][0])
    curr[1][1] = b + max(prev[0][1], prev[1][1], prev[2][1])

    curr[2][0] = c + min(prev[1][0], prev[2][0])
    curr[2][1] = c + max(prev[1][1], prev[2][1])

    prev = curr

max_val = max(p[1] for p in prev)
min_val = min(p[0] for p in prev)
print(max_val, min_val)
