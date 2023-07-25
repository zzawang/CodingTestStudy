baseAZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
base = {i:ord(i)-65 for i in baseAZ}
for a in baseAZ.lower():
    base[a] = ord(a)-71
for n in range(0, 10):
    base[str(n)] = ord(str(n))+4
base["+"] = 62
base["/"] = 63

T = int(input())
for t in range(1, T+1):
    bit = input()
    result = ""
    for i in range(0, len(bit), 4):
        temp = ""
        for k in bit[i:i+4]:
            temp += format(base[k], 'b').zfill(6)
        for m in range(0, len(temp), 8):
            result += chr(int(temp[m:m+8], 2))
    print(f"#{t} {result}")
