def solution(n):
    mlist = []
    for i in range(1, n+1):
        if n%i == 1:
            mlist.append(i)
    return(min(mlist))