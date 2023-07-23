def solution(id_list, report, k):
    answer = {}
    # 본인이 신고한 사람들
    To = {}
    # 본인이 신고받은 횟수
    From = {}
    
    for i in id_list:
        answer[i] = 0
        To[i] = []
        From[i] = 0
        
    for r in report:
        t, f = r.split(' ')
        if f not in To[t]:
            To[t].append(f)
            From[f] += 1
        
    find = []
    for f in From:
        if From[f] >= k:
            find.append(f)
            
    for t1 in To:
        for t2 in To[t1]:
            if t2 in find:
                answer[t1] += 1
    
    return [x for x in answer.values()]