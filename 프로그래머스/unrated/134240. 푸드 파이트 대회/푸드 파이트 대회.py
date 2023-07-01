def solution(food):
    string = ""
    for i in range(1, len(food)):
        string += str(i)*(food[i]//2)
    return string+"0"+string[::-1]