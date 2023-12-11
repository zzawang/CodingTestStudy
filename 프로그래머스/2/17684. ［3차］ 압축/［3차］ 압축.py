def solution(msg):
    my_dict = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, a in enumerate(alpha):
        my_dict[a] = i + 1
        
    answer = []
    index = 0
    count = index + 1
    while index < len(msg):
        count = index + 1 if count <= len(msg) else len(msg)
        while count + 1 <= len(msg) and msg[index:count + 1] in my_dict.keys():
            count += 1
        answer.append(my_dict[msg[index:count]])
        if count + 1 <= len(msg):
            my_dict[msg[index:count + 1]] = len(my_dict) + 1
        index = count
        
    return answer