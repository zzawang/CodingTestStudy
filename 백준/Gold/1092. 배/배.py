import sys

N = int(sys.stdin.readline().rstrip())
crains = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
M = int(sys.stdin.readline().rstrip())
boxes = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)

if boxes[0] > crains[0]:
    print(-1)
else:
    answer = 0
    while boxes:
        for c in crains:
            if boxes and boxes[-1] > c:
                continue
            for b in boxes:
                if b <= c:
                    boxes.remove(b)
                    break

        answer += 1
    print(answer)