def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    report_dict = {}
    report_person_dict = {}
    for id in id_list:
        report_dict[id] = 0
        report_person_dict[id] = []
        
    for r in report:
        report_from, report_to = r.split(" ")
        report_dict[report_to] += 1
        report_person_dict[report_from].append(report_to)
    
    for rpd in report_person_dict.keys():
        count = 0
        for person in report_person_dict[rpd]:
            if report_dict[person] >= k:
                count += 1
        answer.append(count)
    
    return answer