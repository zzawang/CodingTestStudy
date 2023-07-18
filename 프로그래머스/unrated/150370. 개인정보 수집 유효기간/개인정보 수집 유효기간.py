def solution(today, terms, privacies):
    answer = []
    dic = {}
    ty, tm, td = map(int, today.split('.'))
    today = (ty*12*28 + tm*28 + td)
    
    for t in terms:
        a, b = t.split(' ')
        dic[a] = int(b)
        
    for i, p in enumerate(privacies):
        day, types = p.split(' ')
        y, m, d = map(int, day.split('.'))
        # 오늘 날짜가 유효기간에 지났는지 확인하기
        yuho = (y*12*28 + m*28 + d) + dic[types] * 28
        if today >= yuho:
            answer.append(i + 1)
    
    return answer
