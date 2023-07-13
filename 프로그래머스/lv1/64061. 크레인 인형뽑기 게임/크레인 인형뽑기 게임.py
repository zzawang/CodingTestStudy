def solution(board, moves):
    answer = []
    count = 0
    
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if answer and answer[-1] == b[m-1]:
                    count += 2
                    answer.pop()
                else:
                    answer.append(b[m-1])
                b[m-1] = 0
                break
    return count