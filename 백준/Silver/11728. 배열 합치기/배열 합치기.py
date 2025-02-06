a, b = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

ap = 0
bp = 0
answer = []

while ap <= a and bp <= b:
    if bp == b:
        answer.extend(a_arr[ap:])
        break
    elif ap == a:
        answer.extend(b_arr[bp:])
        break
    else:
        if a_arr[ap] < b_arr[bp]:
            answer.append(a_arr[ap])
            ap += 1
        else:
            answer.append(b_arr[bp])
            bp += 1

print(" ".join(str(a) for a in answer))