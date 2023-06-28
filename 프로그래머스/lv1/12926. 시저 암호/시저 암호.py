def solution(s, n):
    answer = ''
    for v in s:
        if v == " ":
            answer += v
            continue
        if v.isupper():
            new_v = chr(ord(v) + n - 26) if ord(v) + n >= 91 else chr(ord(v) + n)
        else:
            new_v = chr(ord(v) + n - 26) if ord(v) + n >= 123 else chr(ord(v) + n)
        answer += new_v
    return answer