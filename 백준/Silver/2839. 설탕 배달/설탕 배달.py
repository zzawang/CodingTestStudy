n = int(input())

five = [-1] * 5001
five[3], five[5] = 0, 1

three = [-1] * 5001
three[3], three[5] = 1, 0

for i in range(3, 5001):
    if five[i - 5] != -1:
        five[i] = five[i - 5] + 1
        three[i] = 0
    if i % 5 != 0 and three[i - 3] != -1:
        three[i] = three[i - 3] + 1
        if five[i] == -1:
            five[i] = 0

if five[n] + three[n] == -2:
    print(-1)
else:
    print(five[n] + three[n])
