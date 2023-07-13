def solution(numbers, hand):
    answer = ''
    distance = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    }
    left = distance['*']
    right = distance['#']
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = distance[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right = distance[n]
        else:
            l = 0
            r = 0
            for a,b,c in zip(left, right, distance[n]):
                l += abs(a-c)
                r += abs(b-c)
            
            if l < r:
                answer += 'L'
                left = distance[n]
            elif r < l:
                answer += 'R'
                right = distance[n]
            else:
                if hand == "left":
                    answer += 'L'
                    left = distance[n]
                else:
                    answer += 'R'
                    right = distance[n]
        
    return answer
