n = 0
m = 0
answer = []

def bt(num):
    global n, m, answer
    if len(answer) == m:
        print(*answer)
        return

    for i in range(num, n + 1):
        if not answer or (answer and answer[-1] <= i):
            answer.append(i)
            bt(num)
            answer.pop()

def solution():
    global n, m
    n, m = map(int, input().split())
    bt(1)

solution()