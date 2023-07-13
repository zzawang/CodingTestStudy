def solution(keymap, targets):
    answer = []
    key = {}
    
    for keys in keymap:
        for i, k in enumerate(keys):
            if k in key.keys() and key[k] < i+1:
                continue
            else:
                key[k] = i+1
                
    for target in targets:
        count = 0
        for t in target:
            if t in key.keys():
                count += key[t]
            else:
                count = -1
                break
            
        answer.append(count)
        
    return answer