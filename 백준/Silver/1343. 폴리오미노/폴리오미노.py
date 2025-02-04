arr = input()
board = []
tmp = ''
for i in range(len(arr) + 1):
    if i == len(arr):
        board.append(tmp)
        break

    if arr[i] == '.':
        if tmp != '':
            board.append(tmp)
        board.append('.')
        tmp = ''
    else:
        tmp += arr[i]

answer = ''
for b in board:
    if b == '.':
        answer += '.'
        continue

    flag = False
    for i in range(len(b) // 4, -1, -1):
        word = ''
        tmp = len(b) - i * 4
        if tmp % 2 == 0:
            word += (i * 'AAAA' + (tmp // 2) * 'BB')
            answer += word
            flag = True
            break

    if not flag:
        print(-1)
        exit()

print(answer)