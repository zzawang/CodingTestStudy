import sys

def div(x, y, n):
    color = paper[x][y]  # 현재 종이의 색깔
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:  # 하나라도 다른 색이 나오면 분할
                m = n//2  # 크기를 반으로 나눔
                div(x, y, m)  # 2사분면 (왼쪽 위)
                div(x, y + m, m)  # 1사분면 (오른쪽 위)
                div(x + m, y, m)  # 3사분면 (왼쪽 아래)
                div(x + m, y + m, m)  # 4사분면 (오른쪽 아래)
                return
    
    # 색종이가 한 가지 색으로 이루어진 경우
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1


N = int(sys.stdin.readline().rstrip())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = [0, 0]  # [흰색 종이 개수, 파란색 종이 개수]
div(0, 0, N)
print(answer[0])
print(answer[1])