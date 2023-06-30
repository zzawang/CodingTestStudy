def solution(n, arr1, arr2):
    new_arr1 = []
    new_arr2 = []
    
    answer = []
    
    for i in arr1:
        v = bin(i)[2:]
        
        if len(v) != n:
            v = "0" * (n - len(v)) + v
            
        new_arr1.append([x for x in v])
        
    for i in arr2:
        v = bin(i)[2:]
        
        if len(v) != n:
            v = "0" * (n - len(v)) + v
            
        new_arr2.append([x for x in v])
    
    for i1, v in enumerate(new_arr1):
        sharp = ""
        for i2, x in enumerate(v):
            if x == '1':
                sharp += "#"
            else:
                if new_arr2[i1][i2] == '1':
                    sharp += "#"
                else:
                    sharp += " "
        answer.append(sharp)
    
    return answer