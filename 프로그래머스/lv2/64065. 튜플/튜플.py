from collections import Counter
def solution(s):
    answer = []
    pre = ''
    for x in s:
        if x.isdigit():
            pre += x
        elif pre.isdigit() and not x.isdigit():
            answer.append(int(pre))
            pre = ''
        
    count = dict(Counter(answer))
    return sorted(count.keys(), reverse = True, key = lambda x:count[x])