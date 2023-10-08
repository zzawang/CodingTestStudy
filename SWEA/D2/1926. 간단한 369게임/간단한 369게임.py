n = int(input())
for i in range(1, n+1):
    answer = ''
    for a in str(i):
        if int(a)%3 == 0 and int(a) != 0:
            answer += '-'
    answer = i if answer == '' else answer
    print(answer, end=' ')