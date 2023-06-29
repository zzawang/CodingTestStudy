def solution(t, p):
    t_list = []
    for i in range(len(t) - len(p) + 1):
        t_list.append(int(t[i:i + len(p)]))
    
    return len([x for x in t_list if x <= int(p)])