def solution(s):
    str = s.lower()
    return True if str.count('p') == str.count('y') or (str.count('p') == 0 and str.count('y') == 0) else False
