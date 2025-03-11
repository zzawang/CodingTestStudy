import sys

# 도시의 개수 N, 최대 방문 도시의 개수 M, 개설된 항공로의 개수 K
N, M, K = map(int, sys.stdin.readline().rstrip().split())

route = [[0] * N for _ in range(N)]  # 0인 경우 경로 X
for _ in range(K):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    route[a - 1][b - 1] = max(route[a - 1][b - 1], c)

# i번 도시까지 j개의 도시를 지나며 먹는 기내식 점수 총 합의 최대값
dp = [[-1] * M for _ in range(N)]

dp[0][0] = 0  # 1번 도시에서 출발
for i in range(N):  # 현재 도시
    for j in range(M - 1):  # 방문한 도시 수
        if dp[i][j] == -1:
            continue  # 도달할 수 없는 경우 스킵

        for arrival in range(i + 1, N):
            if route[i][arrival] > 0:  # 항로가 존재한다면
                dp[arrival][j + 1] = max(dp[arrival][j + 1], dp[i][j] + route[i][arrival])

print(max(dp[-1]))