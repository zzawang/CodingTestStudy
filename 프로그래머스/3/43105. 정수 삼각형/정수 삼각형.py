def solution(triangle):
    height = len(triangle)
    routes = [[0] * height for h in range(height)] # 각 경로를 거쳐가는 숫자의 최대 합을 저장

    for x in range(height):
        for y, num in enumerate(triangle[x]):
            if x == 0: # 맨 꼭대기는 거쳐간 숫자의 합이 자기 자신
                routes[x][y] = triangle[x][y]
            else:
                possible = [] # 가능한 경로의 숫자의 합들
                if 0 <= x - 1 and x - 1 < height and 0 <= y and y < height:
                    possible.append(routes[x-1][y])
                if 0 <= x - 1 and x - 1 < height and 0 <= y - 1 and y - 1 < height:
                    possible.append(routes[x-1][y-1])
                    
                routes[x][y] = triangle[x][y] + max(possible)
                    
    return max(routes[height - 1])
    