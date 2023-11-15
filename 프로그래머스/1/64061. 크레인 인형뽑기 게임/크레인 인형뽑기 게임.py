def crain(n, board):
    length = len(board)
    find = 0
    for i in range(length):
        if board[i][n] != 0:
            find = board[i][n]
            board[i][n] = 0
            break
            
    return find

def solution(board, moves):
    answer = 0
    dolls = []
    for m in moves:
        doll = crain(m-1, board)
        if dolls and dolls[-1] == doll:
            dolls.pop()
            answer += 2
        elif doll != 0:
            dolls.append(doll)
        
    return answer