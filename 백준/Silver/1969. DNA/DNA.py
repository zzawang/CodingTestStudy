from collections import Counter

def solution():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(input())

    hd = 0
    dna = ''
    for j in range(m):
        tmp = ''
        for i in range(n):
            tmp += arr[i][j]

        max_letter_count = -1
        for key, value in sorted(dict(Counter(tmp)).items(), key=lambda x:(-x[1], x[0])):
            if max_letter_count < value:
                max_letter_count = value
                dna += key
            else:
                hd += value

    print(dna)
    print(hd)

solution()