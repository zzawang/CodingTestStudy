import math
def solution(fees, records):
    answer = []
    in_times = {} # 각 차량별 입차 시간
    times = {} # 각 차량별 누적 시간
        
    for r in records:
        time, car, state = r.split(" ")
        h, m = map(int, time.split(":"))
        if state == "OUT":
            if car not in times.keys():
                times[car] = h*60 + m - in_times[car]
            else:
                times[car] += h*60 + m - in_times[car]
            in_times[car] = -1
        else:
            in_times[car] = h*60 + m
    
    for it in in_times.keys():
        if in_times[it] != -1:
            if it not in times.keys():
                times[it] = 23*60 + 59 - in_times[it]
            else:
                times[it] += 23*60 + 59 - in_times[it]
    
    times = dict(sorted(times.items(), key = lambda x:x[0]))
    for fee in times.values():
        if fee > fees[0]:
            result = fees[1] + math.ceil((fee - fees[0])/fees[2]) * fees[3]
            answer.append(result)
        else:
            answer.append(fees[1])
    
    return answer