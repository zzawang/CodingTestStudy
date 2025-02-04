from itertools import combinations

h, w = map(int, input().split())
n = int(input())
stickers = []
for _ in range(n):
    stickers.append(tuple(map(int, input().split())))

answer = 0
for stickerA, stickerB in list(combinations(stickers, 2)):
    flag = False
    stickerA_w, stickerA_h = stickerA
    stickerB_w, stickerB_h = stickerB
    if stickerA_w + stickerB_w <= w and max(stickerA_h, stickerB_h) <= h:
        flag = True
    elif stickerA_w + stickerB_h <= w and max(stickerA_h, stickerB_w) <= h:
        flag = True
    elif stickerA_h + stickerB_w <= w and max(stickerA_w, stickerB_h) <= h:
        flag = True
    elif stickerA_h + stickerB_h <= w and max(stickerA_w, stickerB_w) <= h:
        flag = True
    elif stickerA_w + stickerB_w <= h and max(stickerA_h, stickerB_h) <= w:
        flag = True
    elif stickerA_w + stickerB_h <= h and max(stickerA_h, stickerB_w) <= w:
        flag = True
    elif stickerA_h + stickerB_w <= h and max(stickerA_w, stickerB_h) <= w:
        flag = True
    elif stickerA_h + stickerB_h <= h and max(stickerA_w, stickerB_w) <= w:
        flag = True

    result = stickerA_w * stickerA_h + stickerB_w * stickerB_h
    if flag and h * w >= result:
        answer = max(answer, result)

print(answer)