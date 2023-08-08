def solution(arr1, arr2):
    arr = []
    for a in arr1:
        t1 = 0
        t2 = 0
        li = []
        for _ in range(len(arr2[0])):
            sum = 0
            for a1 in a:
                sum += (a1 * arr2[t1][t2])
                t1 += 1
            li.append(sum)
            t2 += 1
            t1 = 0
        arr.append(li)
    return arr