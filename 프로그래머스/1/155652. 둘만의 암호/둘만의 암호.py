def solution(s, skip, plus):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for string in s:
        index = alphabet.index(string)
        count = 0
        a = 0
        while (count < plus):
            a += 1
            if alphabet[(index + a)%len(alphabet)] not in skip:
                count += 1
        answer += alphabet[(index + a)%len(alphabet)]
                
    return answer