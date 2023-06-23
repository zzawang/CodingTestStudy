def solution(arr1, arr2):
    answer1 = []
    zlist1 = zip(arr1, arr2)
    for v1, v2 in zlist1:
        answer2 = []
        zlist2 = zip(v1, v2)
        for z1, z2 in zlist2:
            answer2.append(z1 + z2)
        answer1.append(answer2)   
            
    return answer1