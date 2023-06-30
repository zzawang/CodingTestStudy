# def solution(strings, n):
#     strings.sort()
    
#     for i in range(len(strings) - 1):
#         if strings[i][n] > strings[i + 1][n]:
#             strings[i], strings[i + 1] = strings[i + 1], strings[i]
    
#     return strings

def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i] 
    strings.sort()
    return [x[1:] for x in strings]