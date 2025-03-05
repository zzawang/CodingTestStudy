import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    stickers = []
    for i in range(2):
        stickers.append(list(map(int, sys.stdin.readline().rstrip().split())))

    if N > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

        for i in range(2, N):
            stickers[0][i] += max(stickers[1][i - 1], stickers[1][i - 2])
            stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])

    print(max(stickers[0][-1], stickers[1][-1]))
