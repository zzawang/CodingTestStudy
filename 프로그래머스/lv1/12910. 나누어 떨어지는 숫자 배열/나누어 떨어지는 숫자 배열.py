def solution(arr, divisor):
    arr = [i for i in arr if i%divisor == 0]
    if arr != []:
        return sorted(arr)
    else:
        arr.append(-1)
        return arr