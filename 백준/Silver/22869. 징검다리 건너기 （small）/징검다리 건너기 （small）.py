import sys

N, K = map(int, sys.stdin.readline().rstrip().split())  # 돌의 개수 N, 쓸 수 있는 최대 힘 K
A = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [False] * N
dp[0] = True

for i in range(N):
    for j in range(i + 1, N):
        power = (j - i) * (1 + abs(A[i] - A[j]))
        if dp[i] and power <= K:
            dp[j] = True


if dp[-1]:
    print("YES")
else:
    print("NO")

