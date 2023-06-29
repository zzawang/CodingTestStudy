def solution(s):
    alphadict = {"0" : "zero", "1" : "one", "2" : "two", "3" : "three", 
                 "4" : "four", "5" : "five", "6" : "six", "7" : "seven",
                 "8" : "eight", "9" : "nine"}
    
    for i in alphadict.keys():
        if alphadict[i] in s:
            s = s.replace(alphadict[i], i)
    return int(s)