def solution(m, n, puddles):
    puddles = [[x - 1, y - 1] for [y, x] in puddles]
    dp = [[0] * m for index in range(n)] 
    dp[0][0] = 1  # 집 위치 

    for x in range(n):
        for y in range(m):
            if x == 0 and y == 0: # 집 위치일 경우
                continue 
            if [x, y] in puddles: # 웅덩이 위치일 경우
                dp[x][y] = 0
            else:
                dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007
                
    return dp[n - 1][m - 1]
