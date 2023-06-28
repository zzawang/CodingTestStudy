def solution(sizes):
    max_num = 0
    max_index = -1
    
    for i in sizes:
        if max_num < max(i):
            max_num = max(i)
            max_index = i.index(max(i))
    
    if max_index == 0:
        for i in sizes:
            i.sort(reverse = True)
    else:
        for i in sizes:
            i.sort()
        
    min_index = 0 if max_index == 1 else 1
    
    return max(i[max_index] for i in sizes) * max(i[min_index] for i in sizes)