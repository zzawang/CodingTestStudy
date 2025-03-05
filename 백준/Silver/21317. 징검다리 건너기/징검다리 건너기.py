import sys

n = int(sys.stdin.readline())  # 돌 개수
jumps = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]
k = int(sys.stdin.readline())  # 매우 큰 점프의 에너지

def min_energy_to_cross(n, jumps, k):
    INF = float('inf')
    DP = [[INF] * 2 for _ in range(n + 1)]
    DP[1][0] = 0  # 첫 번째 돌에서 시작하는 에너지는 0

    for i in range(1, n):
        if i + 1 <= n:
            DP[i + 1][0] = min(DP[i + 1][0], DP[i][0] + jumps[i - 1][0])
            DP[i + 1][1] = min(DP[i + 1][1], DP[i][1] + jumps[i - 1][0])
        if i + 2 <= n:
            DP[i + 2][0] = min(DP[i + 2][0], DP[i][0] + jumps[i - 1][1])
            DP[i + 2][1] = min(DP[i + 2][1], DP[i][1] + jumps[i - 1][1])
        if i + 3 <= n:
            DP[i + 3][1] = min(DP[i + 3][1], DP[i][0] + k)

    return min(DP[n][0], DP[n][1])

print(min_energy_to_cross(n, jumps, k))
