a, b = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

ap = 0
bp = 0
answer = []
length = 0

while length < a + b:
    if bp == b or (ap < a and a_arr[ap] < b_arr[bp]):
        answer.append(a_arr[ap])
        ap += 1
    elif ap == a or (bp < b and a_arr[ap] > b_arr[bp]):
        answer.append(b_arr[bp])
        bp += 1
    else:
        answer.append(a_arr[ap])
        answer.append(b_arr[bp])
        ap += 1
        bp += 1
        length += 1
    length += 1

print(" ".join(str(a) for a in answer))