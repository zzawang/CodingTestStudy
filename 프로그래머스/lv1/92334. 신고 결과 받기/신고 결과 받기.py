def solution(id_list, report, k):
    
    id_dict = {}
    report_dict = {}
    
    for id in id_list:
        id_dict[id] = 0
        report_dict[id] = list()
        # {"muzi" : ["xx", "dd"], "frodo" : ["dd"]} .. 이런식
    
    for content in report:
        a, b = content.split(" ")
        # 자기 자신을 신고한 사람을 추가
        if a not in report_dict[b]:
            report_dict[b].append(a)
            
    for i in report_dict:
        if len(report_dict[i]) >= k:
            for x in report_dict[i]:
                id_dict[x] += 1
            
    answer = []
    
    for p in id_dict:
        answer.append(id_dict[p])
        
    return answer