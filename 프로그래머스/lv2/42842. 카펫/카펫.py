def solution(brown, yellow):
    yellow_list = [] if yellow != 1 else [(1, 1)]
    
    # 노란색을 만들 수 있는 경우의 수(가로가 세로보다 같거나 길게)에서
    # (가로 + 세로)*n = 갈색 - 4 여야 함
    # 이 n을 노란색을 만들 수 있는 경우의 수에 각각 더해 주면 정답
    
    # 노란색을 만들 수 있는 경우의 수
    for i in range(1, yellow//2 + 1):
        if yellow%i == 0:
            max_n = max(yellow//i, i)
            min_n = min(yellow//i, i)
            if (max_n, min_n) not in yellow_list:
                yellow_list.append((max_n, min_n))
    
    for w, h in yellow_list:
        if (brown - 4)%(w + h) == 0:
            n = (brown - 4)//(w + h)
            return [w + n, h + n]
    