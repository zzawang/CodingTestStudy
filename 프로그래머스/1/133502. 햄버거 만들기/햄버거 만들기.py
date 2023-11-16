def solution(ingredient):
    answer = 0
    hamburger = [1,2,3,4]
    
    for i in ingredient:
        hamburger.append(i)
        if len(hamburger) >= 4 and hamburger[-4:] == [1, 2, 3, 1]:
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
            hamburger.pop()
            answer += 1
            
    return answer