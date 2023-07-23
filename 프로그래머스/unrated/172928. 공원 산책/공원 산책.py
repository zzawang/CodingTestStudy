def solution(park, routes):
    answer = []
    first = []

    X = len(park)
    Y = 0
    
    for i1, p1 in enumerate(park):
        Y = len(p1)
        for i2, p2 in enumerate(p1):
            if p2 == 'S':
                first = [i1, i2]
    
    answer = first
    for r in routes:
        direction, distance = r.split(' ')
        distance = int(distance)
        v = answer
        flag = 0
        if direction == 'E':
            for i in range(1, distance+1):
                x, y = v[0], v[1] + i
                if (x >= X or x < 0 or y < 0 or y >= Y) or (park and park[x][y] == 'X'):
                    flag = 1
                    break
            if flag == 0:
                answer = [x, y]
                    
        elif direction == 'W':
            for i in range(1, distance+1):
                x, y = v[0], v[1] - i
                if (x >= X or x < 0 or y < 0 or y >= Y) or (park and park[x][y] == 'X'):
                    flag = 1
            if flag == 0:
                answer = [x, y]
        elif direction == 'N':
            for i in range(1, distance+1):
                x, y = v[0] - i, v[1]
                if (x >= X or x < 0 or y < 0 or y >= Y) or (park and park[x][y] == 'X'):
                    flag = 1
                    break
            if flag == 0:
                answer = [x, y]
        elif direction == 'S':
            for i in range(1, distance+1):
                x, y = v[0] + i, v[1]
                if (x >= X or x < 0 or y < 0 or y >= Y) or (park and park[x][y] == 'X'):
                    flag = 1
            if flag == 0:
                answer = [x, y]
        
    return answer