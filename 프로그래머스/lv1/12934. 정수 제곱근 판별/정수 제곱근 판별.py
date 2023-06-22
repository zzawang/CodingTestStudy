import math
def solution(n):
    if int(str(math.sqrt(n)).split(".")[1]) > 0:
        return -1
    else:
        return (math.sqrt(n) + 1)*(math.sqrt(n) + 1)