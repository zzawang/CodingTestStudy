from collections import deque
def main():
    visited = [False]*100001
    n, k = map(int, input().split())
    if n == k:
        print(0)
        return
    depth = 0
    q = deque([(depth, n)])
    visited[n] = True

    while q:
        d, num = q.popleft()
        depth = d + 1
        if num * 2 == k or num - 1 == k or num + 1 == k:
            print(depth)
            break

        if num * 2 <= 100000 and not visited[num * 2]:
            q.append((depth, num * 2))
            visited[num * 2] = True
        if num - 1 >= 0 and not visited[num - 1]:
            q.append((depth, num - 1))
            visited[num - 1] = True
        if num + 1 <= 100000 and not visited[num + 1]:
            q.append((depth, num + 1))
            visited[num + 1] = True

main()