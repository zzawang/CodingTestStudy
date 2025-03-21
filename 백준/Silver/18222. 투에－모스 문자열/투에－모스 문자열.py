import sys

def thue_morse(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    elif idx % 2 == 0:
        return thue_morse(idx // 2)
    else:
        return 1 - thue_morse(idx // 2)

K = int(sys.stdin.readline().rstrip())
print(thue_morse(K - 1))
