def solution(str1, str2):
    A_list = []
    B_list = []
    
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            A_list.append(str1[i:i+2].lower())
        
    for i in range(len(str2) - 1):
        if str2[i:i+2].isalpha():
            B_list.append(str2[i:i+2].lower())
    
    intersection = set(A_list) & set(B_list)
    union = set(A_list) | set(B_list)
    
    intersection_sum = sum([min(A_list.count(u), (B_list.count(u))) for u in intersection])
    union_sum = sum([max(A_list.count(i), (B_list.count(i))) for i in union])
                
    if union_sum == 0:
        return 65536
    else:
        return int((intersection_sum / union_sum) * 65536)