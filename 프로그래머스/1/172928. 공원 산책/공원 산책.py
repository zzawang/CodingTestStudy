dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(park, start, index, n):
    for i in range(1, n + 1):
        px = start[0] + (dx[index] * i)
        py = start[1] + (dy[index] * i)
        if px < 0 or px >= len(park) or py < 0 or py >= len(park[0]):
            return False
        if park[px][py] == "X":
            return False
    
    return True

def solution(park, routes):
    for i1 in range(len(park)):
        for i2 in range(len(park[0])):
            if park[i1][i2] == "S":
                start = [i1, i2]
    
    for r in routes:
        op, num = r.split(" ")
        n = int(num)
        if op == "N":
            if check(park, start, 0, n):
                start[0] += (n * dx[0])
                start[1] += (n * dy[0])
        elif op == "S":
            if check(park, start, 1, n):
                start[0] += (n * dx[1])
                start[1] += (n * dy[1])
        elif op == "W":
            if check(park, start, 2, n):
                start[0] += (n * dx[2])
                start[1] += (n * dy[2])
        else:
            if check(park, start, 3, n):
                start[0] += (n * dx[3])
                start[1] += (n * dy[3])
    
    return start