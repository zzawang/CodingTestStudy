def solution(s):
    if len(s) == 4 or len(s) == 6:
        for index in s:
            if index.isalpha():
                return False
        return True
    else:
        return False