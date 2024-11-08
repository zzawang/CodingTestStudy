from itertools import combinations, product
from bisect import bisect_left

def solution(dicesArr):
    answer = []
    dices = {} # 각 주사위 별 숫자 정보
    for index, dice in enumerate(dicesArr):
        dices[index + 1] = dice
        
    dice_combination = [] # A, B의 모든 주사위 경우의 수
    dice_length = len(dicesArr) # 총 주사위의 수
    each_length = dice_length // 2 # 각자 가져갈 수 있는 주사위의 수
    
    for A_combination in combinations(range(1, dice_length + 1), each_length):
        B_combination = [dice_num for dice_num in range(1, dice_length + 1) if dice_num not in A_combination]
        dice_combination.append((list(A_combination), B_combination))
            
    score = []
    max_win_count = -1
    for A_combination, B_combination in dice_combination:
        win_count = 0
        A_dice_nums = [dices[A_dice] for A_dice in A_combination]
        B_dice_nums = [dices[B_dice] for B_dice in B_combination]
        
        A_scores = sorted(sum(result) for result in product(*A_dice_nums))
        B_scores = sorted(sum(result) for result in product(*B_dice_nums))
        
        for A_score in A_scores:
            win_count += bisect_left(B_scores, A_score)
            
        if win_count > max_win_count:
            max_win_count = win_count
            answer = A_combination
        
    return answer