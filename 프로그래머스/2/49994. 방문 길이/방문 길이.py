dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(dirs):
    answer = 0
    visited = [[[] for _ in range(11)] for _ in range(11)]
    x, y = 5, 5
    
    for d in dirs:
        if d == "U":
            nx, ny = x + dx[0], y + dy[0]
        elif d == "D":
            nx, ny = x + dx[1], y + dy[1]
        elif d == "L":
            nx, ny = x + dx[2], y + dy[2]
        elif d == "R":
            nx, ny = x + dx[3], y + dy[3]
        
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if (x, y) not in visited[nx][ny] and (nx, ny) not in visited[x][y]:
                answer += 1
                visited[x][y].append((nx, ny))
                visited[nx][ny].append((x, y))
            x, y = nx, ny
    return answer