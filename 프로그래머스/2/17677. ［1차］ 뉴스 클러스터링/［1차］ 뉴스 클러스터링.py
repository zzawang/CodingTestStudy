def solution(str1, str2):
    str1 = str1.lower();
    str2 = str2.lower();
    A_list = []
    B_list = []
    intersection = []
    union = []
    
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            A_list.append(str1[i:i+2])
        
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            B_list.append(str2[i:i+2])
            
    for s1 in A_list:
        if s1 not in intersection:
            for _ in range(min(A_list.count(s1), B_list.count(s1))):
                intersection.append(s1)
                
        if s1 not in union:
            for _ in range(max(A_list.count(s1), B_list.count(s1))):
                union.append(s1)
                
    for s1 in B_list:
        if s1 not in intersection:
            for _ in range(min(A_list.count(s1), B_list.count(s1))):
                intersection.append(s1)
                
        if s1 not in union:
            for _ in range(max(A_list.count(s1), B_list.count(s1))):
                union.append(s1)
    
    if not union:
        answer = 1
    else:
        answer = len(intersection) / len(union)
    return int(answer * 65536)