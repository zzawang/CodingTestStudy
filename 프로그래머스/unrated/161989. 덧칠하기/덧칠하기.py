def solution(n, m, section):
    new_m = m
    count = 0
    flag = False  # 0을 만났을 시
    wall = [1] * n  # 처음에는 다 칠해져 있다고 가정
    
    for x in section:  # 안 칠해진 부분 표시
        wall[x-1] = 0 
        
    for i, v in enumerate(wall):
        if new_m == 0:
            new_m = m
            flag = False
        if v == 0 and flag == False:
            flag = True  # 0 만남
            wall[i] = 1
            count += 1
            new_m -= 1
        elif flag == True:
            wall[i] = 1
            new_m -= 1
    return count