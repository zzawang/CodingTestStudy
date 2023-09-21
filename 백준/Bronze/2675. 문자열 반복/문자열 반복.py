for _ in range(int(input())):
    a, b = input().split()
    text = ""
    for i in range(len(b)):
        text += b[i]*int(a)
    print(text)