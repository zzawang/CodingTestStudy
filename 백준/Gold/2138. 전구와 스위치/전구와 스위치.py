def click(light, target):
    count = 0
    for i in range(1, n):
        if light[i - 1] == target[i - 1]:
            continue

        count += 1
        for j in range(i - 1, i + 2):
            if j < n:
                light[j] = 1 - light[j]

    return count if light == target else float("inf")

n = int(input())
light = list(map(int, input()))
target = list(map(int, input()))

ans = click(light[:], target)

light[0] = 1 - light[0]
light[1] = 1 - light[1]
ans = min(ans, click(light[:], target) + 1)
print(ans if ans != float("inf") else -1)