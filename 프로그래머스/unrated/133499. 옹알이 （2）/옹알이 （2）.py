def solution(babbling):
    answer = 0
    
    for v in babbling:
        start = 0
        pre = ''
        while True:
            if v[start:start+3] == "aya" and "aya" != pre:
                start += 3
                pre = "aya"
            elif v[start:start+3] == "woo" and "woo" != pre:
                start += 3
                pre = "woo"
            elif v[start:start+2] == "ye" and "ye" != pre:
                start += 2
                pre = "ye"
            elif v[start:start+2] == "ma" and "ma" != pre:
                start += 2
                pre = "ma"
            else:
                break
            
            if start >= len(v):
                answer += 1
                break
            
    return answer