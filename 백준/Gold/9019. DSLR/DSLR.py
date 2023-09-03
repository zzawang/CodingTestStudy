from collections import deque
import sys

for tc in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    visited = [False] * 10000
    q = deque([(A, '')])
    visited[A] = True

    while q:
        n, c = q.popleft()
        if n == B:
            print(c)
            break

        arr = []
        # D
        a = n*2
        if a > 9999:
            a %= 10000
        arr.append((a, c + 'D'))
        # S
        a = 9999 if n == 0 else n - 1
        arr.append((a, c + 'S'))

        n = (4-len(str(n)))*'0' + str(n)
        # L
        a = int(n[1:] + n[0])
        arr.append((a, c + 'L'))
        # R
        a = int(n[-1] + n[:len(n)-1])
        arr.append((a, c + 'R'))
        for m, char in arr:
            if 0 <= m < 10000 and not visited[m]:
                visited[m] = True
                q.append((m, char))