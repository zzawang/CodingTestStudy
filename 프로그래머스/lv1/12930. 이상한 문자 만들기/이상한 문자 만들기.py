def solution(s):
    s_list = []
    for value in s.split(" "):
        new_v = ''
        for i, v in enumerate(value):
            if i%2 == 0:
                new_v += v.upper()
            else:
                new_v += v.lower()
        s_list.append(new_v)
        
    return ' '.join(s_list)