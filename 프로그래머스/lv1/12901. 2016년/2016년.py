def solution(a, b):
    cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    days = 0
    
    for i in range(a - 1):
        days += cal[i]
    
    days += b
    return day[days%7 - 1]