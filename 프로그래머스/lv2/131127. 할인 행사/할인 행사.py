def solution(want, number, discount):
    answer = 0
    dic = {}
    for a, b in zip(want, number):
        dic[a] = b
    for i in range(len(discount) - 9):
        flag = 1
        arr = discount[i:i+10]
        for d in dic.keys():
            if dic[d] != arr.count(d):
                flag = 0
                break
        if flag == 1:
            answer += 1
            
    return answer