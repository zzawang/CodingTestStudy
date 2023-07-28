T = int(input())
for t in range(1, T + 1):
    n = str(input())
    check = 1 if n[:len(n)//2] == n[-(len(n)//2):][::-1] else 0
    print(f"#{t} {check}")