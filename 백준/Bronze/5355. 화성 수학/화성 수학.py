tc = []
for _ in range(int(input())):
    tc.append(input().split())

for value in tc:
    n = float(value[0])
    for i in range(1, len(value)):
        if value[i] == "@":
            n *= 3
        elif value[i] == "%":
            n += 5
        elif value[i] == "#":
            n -= 7
        else:
            pass
    # 이렇게 하니까 소수점 둘째 자리까지 "0이 더 붙어서" 나오지는 않음!!
    # print(round(n, 5)) 
    print(f'{n:.2f}')