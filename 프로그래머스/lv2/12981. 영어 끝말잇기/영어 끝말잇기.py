def solution(n, words):
    word = []  # 사용된 단어 
    pre = words[0][0]
    
    for i, w in enumerate(words):
        if pre == w[0] and w not in word:
            pre = w[-1]
            word.append(w)
            continue
        else:
            return [i%n+1, i//n+1]

    return [0, 0]