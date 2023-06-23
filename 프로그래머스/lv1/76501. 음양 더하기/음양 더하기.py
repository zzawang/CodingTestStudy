def solution(absolutes, signs):
    total_sum = 0
    for i in range(len(absolutes)):
        if not signs[i]:
            total_sum += -absolutes[i]
        else:
            total_sum += absolutes[i]
            
    return total_sum