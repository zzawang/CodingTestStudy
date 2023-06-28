def solution(number):
    count = 0
    for i1 in range(len(number)):
        for i2 in range(i1 + 1, len(number)):
            for i3 in range(i2 + 1, len(number)):
                if number[i1] + number[i2] + number[i3] == 0:
                    count += 1
                
    return count