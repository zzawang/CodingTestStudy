def findK(number, k):
    arr = [s for s in str(number)]
    if len(arr) == 1:
        arr.append('0')

    if str(k) not in arr:
        return False
    return True

n, k = map(int, input().split())
answer = 0

for h in range(0, n + 1):
    for m in range(0, 60):
        for s in range(0, 60):
            if findK(h, k) or findK(m, k) or findK(s, k):
                answer += 1

print(answer)
