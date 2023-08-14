def solution(s):
    answer = []
    pre = ''
    for x in s:
        if x.isdigit():
            pre += x
        elif pre.isdigit() and not x.isdigit():
            answer.append(pre)
            pre = ''
        
    count = [int(x) for x in set(answer)]
    dic = {}
    for c in count:
        dic[c] = answer.count(str(c))
        
    return sorted(dic.keys(), reverse = True, key = lambda x:dic[x])