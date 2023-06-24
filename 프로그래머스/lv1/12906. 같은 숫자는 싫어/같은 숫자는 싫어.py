def solution(arr):
    new_arr = []
    pre = -1
    for v in arr:
        if pre != v:
            new_arr.append(v)
            pre = v
    return new_arr