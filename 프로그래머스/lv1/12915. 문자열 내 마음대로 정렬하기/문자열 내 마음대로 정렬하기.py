def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i] 
    strings.sort()
    
    return [x[1:] for x in strings]