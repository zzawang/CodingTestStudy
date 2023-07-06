def solution(lottos, win_nums):
    correct = 0
    zero = 0
    award = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for v in lottos:
        if win_nums.count(v) == 1:
            correct += 1
        if v == 0:
            zero += 1
    
    return [award[correct + zero], award[correct]]