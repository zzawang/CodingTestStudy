def paint_rect(start_row, start_col, board):
    paint_white = 0
    white_rect = ['WBWBWBWB', 'BWBWBWBW']

    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != white_rect[i % 2][j]:
                paint_white += 1

    return min(paint_white, 64 - paint_white)

def solution():
    answer = 100
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append([rect for rect in input()])

    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            count = paint_rect(i, j, board)
            answer = min(count, answer)

    print(answer)

solution()